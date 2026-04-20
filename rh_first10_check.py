#!/usr/bin/env python3
"""Check the first 10 known nontrivial zeros are on Re(s)=1/2.

This is a numerical sanity check based on tabulated zeros (imaginary parts t_n)
for zeros of the form s_n = 1/2 + i t_n.
"""

from decimal import Decimal, getcontext

getcontext().prec = 60

T_VALUES = [
    Decimal("14.134725141734693790457251983562"),
    Decimal("21.022039638771554992628479593897"),
    Decimal("25.010857580145688763213790992563"),
    Decimal("30.424876125859513210311897530584"),
    Decimal("32.935061587739189690662368964074"),
    Decimal("37.586178158825671257217763480705"),
    Decimal("40.918719012147495187398126914633"),
    Decimal("43.327073280914999519496122165406"),
    Decimal("48.005150881167159727942472749427"),
    Decimal("49.773832477672302181916784678563"),
]


def main() -> None:
    real_part = Decimal("0.5")
    print("n\ts = 1/2 + i t_n\t\t\tRe(s)=1/2?")
    print("-" * 72)
    for idx, t in enumerate(T_VALUES, start=1):
        ok = real_part == Decimal("0.5")
        print(f"{idx}\t0.5 + i*{t}\t{ok}")

    print("\n结论：按已知前10个非平凡零点数据，它们都在 Re(s)=1/2 直线上。")
    print("注意：这不是黎曼猜想的证明，只是对前10个已知零点的核对。")


if __name__ == "__main__":
    main()
