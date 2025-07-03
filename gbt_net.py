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



class SwinTransformer_new(SwinTransformer):
    def proj_out(self, x, normalize=False):
        if normalize:
            x_shape = x.size()
            if len(x_shape) == 5:
                n, ch, d, h, w = x_shape
                x = rearrange(x, "n c d h w -> n d h w c")
                x = F.layer_norm(x, [ch])
                x = rearrange(x, "n d h w c -> n c d h w")
            elif len(x_shape) == 4:
                n, ch, h, w = x_shape
                x = rearrange(x, "n c h w -> n h w c")
                x = F.layer_norm(x, [ch])
                x = rearrange(x, "n h w c -> n c h w")
        
        x = x.flatten(2).transpose(1, 2)
        return x
    

if __name__ == "__main__":
        
    model = SwinTransformer_new(in_chans=1, embed_dim=48, window_size=(7, 7, 7), 
                                patch_size=(2, 2, 2), depths=(2, 2, 2, 2), num_heads=(3, 6, 12, 24))
    x = torch.randn(1, 1, 64, 64, 64)
    out = model(x)
    print(out.shape)
