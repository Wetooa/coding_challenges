use rayon::prelude::*;
use std::env;

fn main() {
    fn ways_to_put_n_queens(n: usize) -> usize {
        fn solve(row: usize, n: usize, cols: usize, rdiag: usize, ldiag: usize) -> usize {
            if row == n {
                return 1;
            }

            let mut count = 0;

            let mut avail = ((1 << n) - 1) & !(cols | rdiag | ldiag);

            while avail != 0 {
                let col_bit = avail & avail.wrapping_neg();
                avail ^= col_bit;

                count += solve(
                    row + 1,
                    n,
                    cols | col_bit,
                    (rdiag | col_bit) >> 1,
                    (ldiag | col_bit) << 1,
                );
            }
            count
        }

        let mut res = (0..(n / 2))
            .into_par_iter()
            .map(|col| {
                solve(
                    1,
                    n,
                    1 << col,
                    match col {
                        0 => 0,
                        _ => 1 << (col - 1),
                    },
                    1 << (col + 1),
                )
            })
            .sum();
        res *= 2;

        if n & 1 == 1 {
            let mid = n / 2;
            res += solve(1, n, 1 << mid, 1 << (mid - 1), 1 << (mid + 1));
        }

        res
    }

    let arg = env::args().nth(1).expect("Expected an integer argument");
    let n = arg.parse().expect("Invalid integer argument");
    let res = ways_to_put_n_queens(n);

    println!("{res} ways to put {n} queens");
}
