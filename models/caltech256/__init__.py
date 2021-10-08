import functools
from ..attentions import get_attention_module

model_dict = {}

def create_net(args):
    net = None

    attention_module = get_attention_module(args.attention_type)

    if args.attention_type == "se" or args.attention_type == "cbam" or args.attention_type == "gc":
        attention_module = functools.partial(
            attention_module, reduction=float(args.attention_param))
    elif args.attention_type == "eca":
        attention_module = functools.partial(
            attention_module, k_size=int(args.attention_param))
    elif args.attention_type == "wa":
        attention_module = functools.partial(
            attention_module, wavename=args.attention_param)

    net = model_dict[args.arch.lower()](
        num_class=args.num_class,
        attention_module=attention_module
    )

    return net