#!/usr/bin/env python3
# Copyright (c) Facebook, Inc. and its affiliates. All Rights Reserved


"""
This directory contains modules for implementing a productionized RoBERTa model.
These modules implement the same Transformer components that are implemented in
the fairseq library, however they're distilled down to just the elements which
are used in the final RoBERTa model, and within that are restructured and
rewritten to be able to be compiled by TorchScript for production use cases.

The SentenceEncoder specifically can be used to load model weights directly from
the publicly release RoBERTa weights, and it will translate these weights to
the corresponding values in this implementation.
"""

from pytorch.text.fb.nn.modules.multihead_attention import MultiheadSelfAttention
from pytorch.text.fb.nn.modules.positional_embedding import PositionalEmbedding
from pytorch.text.fb.nn.modules.residual_mlp import GeLU, ResidualMLP
from pytorch.text.fb.nn.modules.transformer import (
    PassthroughTransformer,
    SELFIETransformer,
    Transformer,
    TransformerLayer,
    TransformerPrefixLayer,
)

from .luna_attention import LunarCausalAttention, LunarMultiheadAttention
from .luna_sentence_encoder import LunaSentenceEncoder
from .multihead_linear_attention import (
    MultiheadLinearAttention,
    QuantizedMultiheadLinearAttention,
)
from .representation import TransformerRepresentation
from .sentence_encoder import PassthroughEncoder, PostEncoder, SentenceEncoder  # noqa


__all__ = [
    "MultiheadLinearAttention",
    "LunarMultiheadAttention",
    "LunarCausalAttention",
    "LunaSentenceEncoder",
    "QuantizedMultiheadLinearAttention",
    "MultiheadSelfAttention",
    "PassthroughTransformer",
    "PositionalEmbedding",
    "ResidualMLP",
    "SentenceEncoder",
    "PostEncoder",
    "SELFIETransformer",
    "Transformer",
    "TransformerLayer",
    "TransformerRepresentation",
    "GeLU",
    "TransformerPrefixLayer",
]
