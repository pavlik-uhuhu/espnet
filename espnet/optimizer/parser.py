"""Common optimizer default config for multiple backends."""


OPTIMIZER_PARSER_DICT = {}


def register_parser(func):
    """Register arg parser."""
    OPTIMIZER_PARSER_DICT[func.__name__] = func
    return func


@register_parser
def sgd(parser):
    """Add arguments."""
    parser.add_argument('--lr', type=float, default=1.0,
                        help='Learning rate')
    parser.add_argument('--weight-decay', type=float, default=0.0,
                        help='Weight decay')
    return parser


@register_parser
def adam(parser):
    """Add arguments."""
    parser.add_argument('--lr', type=float, default=1e-3,
                        help='Learning rate')
    parser.add_argument('--beta1', type=float, default=0.9,
                        help='Beta1')
    parser.add_argument('--beta2', type=float, default=0.999,
                        help='Beta2')
    parser.add_argument('--weight-decay', type=float, default=0.0,
                        help='Weight decay')
    return parser


@register_parser
def adadelta(parser):
    """Add arguments."""
    parser.add_argument('--rho', type=float, default=0.95,
                        help='Rho')
    parser.add_argument('--eps', type=float, default=1e-8,
                        help='Eps')
    parser.add_argument('--weight-decay', type=float, default=0.0,
                        help='Weight decay')
    return parser
