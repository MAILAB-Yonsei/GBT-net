import torch
import torch.nn as nn
import torch.nn.functional as F
from monai.networks.nets.swin_unetr import PatchMergingV2, SwinTransformer, BasicLayer
from monai.utils import optional_import

from collections.abc import Sequence
from torch.nn import LayerNorm
from monai.networks.blocks import PatchEmbed, UnetrBasicBlock
from monai.utils import look_up_option, optional_import
from timm.models.layers import trunc_normal_

rearrange, _ = optional_import("einops", name="rearrange")

class PatchMergingV3(PatchMergingV2):
    """The `PatchMerging` module previously defined in v0.9.0."""

    def forward(self, x):
        x_shape = x.size()
        if len(x_shape) == 4:
            return super().forward(x)
        if len(x_shape) != 5:
            raise ValueError(f"expecting 5D x, got {x.shape}.")
        b, d, h, w, c = x_shape
        pad_input = (h % 2 == 1) or (w % 2 == 1) or (d % 2 == 1)
        if pad_input:
            x = F.pad(x, (0, 0, 0, w % 2, 0, h % 2, 0, d % 2))
        
        x = x.reshape(b, d//2, 2, h//2, 2, w//2, 2, c).permute(0, 1, 3, 5, 2, 4, 6, 7)
        x = x.flatten(4).contiguous().permute(0, 4, 1, 2, 3).flatten(2).permute(0, 2, 1)
        
        x = self.norm(x)
        x = self.reduction(x)
        x = x.reshape(b, d//2, h//2, w//2, 2*c)
        return x


class SwinTransformer_Classification(SwinTransformer):
    """
    Swin Transformer based on: "Liu et al.,
    Swin Transformer: Hierarchical Vision Transformer using Shifted Windows
    <https://arxiv.org/abs/2103.14030>"
    https://github.com/microsoft/Swin-Transformer
    """

    def __init__(self, out_channels, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.num_features = int(self.embed_dim * 2 ** (self.num_layers))
        self.norm = nn.LayerNorm(self.num_features)
        self.avgpool = nn.AdaptiveAvgPool1d(1)

        self.head = nn.Linear(self.num_features, out_channels)

        self.apply(self._init_weights)

    def _init_weights(self, m):
        if isinstance(m, nn.Linear):
            trunc_normal_(m.weight, std=.02)
            if isinstance(m, nn.Linear) and m.bias is not None:
                nn.init.constant_(m.bias, 0)
        elif isinstance(m, nn.LayerNorm):
            nn.init.constant_(m.bias, 0)
            nn.init.constant_(m.weight, 1.0)
        
    def forward(self, x, normalize=True):
        x0 = self.patch_embed(x)
        x0 = self.pos_drop(x0)
        # x0_out = self.proj_out(x0, normalize)
        if self.use_v2:
            x0 = self.layers1c[0](x0.contiguous())
        x1 = self.layers1[0](x0.contiguous())
        # x1_out = self.proj_out(x1, normalize)
        if self.use_v2:
            x1 = self.layers2c[0](x1.contiguous())
        x2 = self.layers2[0](x1.contiguous())
        # x2_out = self.proj_out(x2, normalize)
        if self.use_v2:
            x2 = self.layers3c[0](x2.contiguous())
        x3 = self.layers3[0](x2.contiguous())
        # x3_out = self.proj_out(x3, normalize)
        if self.use_v2:
            x3 = self.layers4c[0](x3.contiguous())
        x4 = self.layers4[0](x3.contiguous())
        # x4_out = self.proj_out(x4, normalize)
        
        out = x4.flatten(2).permute(0, 2, 1) # B L C
        out = self.norm(out)
        out = self.avgpool(out.transpose(1, 2))  # B C 1
        out = torch.flatten(out, 1)
        out = self.head(out)
                
        return out
        

if __name__ == "__main__":
        
    model = SwinTransformer_new(in_chans=1, embed_dim=48, window_size=(7, 7, 7), 
                                patch_size=(2, 2, 2), depths=(2, 2, 2, 2), num_heads=(3, 6, 12, 24))
    x = torch.randn(1, 1, 64, 64, 64)
    out = model(x)
    print(out.shape)
