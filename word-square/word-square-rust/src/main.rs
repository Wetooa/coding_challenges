pub mod trie;

use rayon::prelude::*;
use std::env;
use std::{
    fs::File,
    io::{BufRead, BufReader},
};
use trie::{Trie, TrieNode};

fn main() -> Result<(), Box<dyn std::error::Error>> {
    let n = env::args()
        .nth(1)
        .expect("Please provide the N of the word square as an argument.")
        .parse::<usize>()
        .expect("Invalid size provided.");

    let m = env::args()
        .nth(2)
        .expect("Please provide the M of the word square as an argument.")
        .parse::<usize>()
        .expect("Invalid size provided.");

    let row_trie = build_trie(m)?;
    let col_trie = build_trie(n)?;

    solve_word_square(&row_trie, &col_trie, n, m);
    Ok(())
}

fn build_trie(size: usize) -> Result<Trie, Box<dyn std::error::Error>> {
    println!("Building {size}'sized trie from file...");

    let mut trie = Trie::new();
    let file = File::open("assets/words_alpha.txt")?;
    let reader = BufReader::new(file);

    for line in reader.lines() {
        let word = line?;
        if word.len() == size {
            trie.insert(&word);
        }
    }

    println!("Trie built with words from file.");
    Ok(trie)
}

// FIX: for somre reason its slower than python :p
fn solve_word_square(row_trie: &Trie, col_trie: &Trie, n: usize, m: usize) {
    println!("Solving word square of size {n}x{m}");
    let row_root = &row_trie.root;
    let col_root = &col_trie.root;

    let mut rows = vec![row_root; n];
    let mut cols = vec![col_root; m];

    fn solve(
        r: usize,
        c: usize,
        rows: &mut Vec<&TrieNode>,
        cols: &mut Vec<&TrieNode>,
        res: &mut Vec<Vec<char>>,
    ) -> bool {
        if r == rows.len() {
            let border = "-".repeat(rows.len() + 2);
            println!("{border}");
            for row in res.iter() {
                let line: String = row.iter().collect();
                println!("|{line}|");
            }
            println!("{border}");
            return true;
        }

        for ch in 'a'..='z' {
            match (rows[r].children.get(&ch), cols[c].children.get(&ch)) {
                (Some(next_row), Some(next_col)) => {
                    let prev_row = rows[r];
                    let prev_col = cols[c];

                    res[r][c] = ch;
                    rows[r] = next_row;
                    cols[c] = next_col;

                    if if cols.len() - 1 == c {
                        solve(r + 1, 0, rows, cols, res)
                    } else {
                        solve(r, c + 1, rows, cols, res)
                    } {
                        return true;
                    }

                    res[r][c] = ' ';
                    rows[r] = prev_row;
                    cols[c] = prev_col;
                }
                _ => continue,
            }
        }

        false
    }

    solve(0, 0, &mut rows, &mut cols, &mut vec![vec![' '; m]; n]);

    // NOTE: Parallelizing ! ! !
    // FIX: doesnt stop after 1 solve lol

    // ('a'..='z').into_par_iter().for_each(|ch| {
    //     let mut res = vec![vec![' '; m]; n];
    //     let mut rows_clone = rows.clone();
    //     let mut cols_clone = cols.clone();
    //
    //     match (
    //         rows_clone[0].children.get(&ch),
    //         cols_clone[0].children.get(&ch),
    //     ) {
    //         (Some(next_row), Some(next_col)) => {
    //             res[0][0] = ch;
    //             rows_clone[0] = next_row;
    //             cols_clone[0] = next_col;
    //
    //             solve(0, 1, &mut rows_clone, &mut cols_clone, &mut res);
    //         }
    //         _ => todo!(),
    //     }
    // });
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_trie_contains() {
        let mut trie = Trie::new();
        trie.insert("hello");
        assert!(trie.contains("hello"));
        assert!(!trie.contains("world"));
    }
}
