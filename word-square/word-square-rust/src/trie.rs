use std::collections::HashMap;

#[allow(dead_code)]
#[derive(Default)]
pub struct TrieNode {
    pub children: HashMap<char, TrieNode>,
    pub is_end_of_word: bool,
}

#[derive(Default)]
#[allow(dead_code)]
pub struct Trie {
    pub root: TrieNode,
}

#[allow(dead_code)]
impl Trie {
    pub fn new() -> Self {
        Self::default()
    }

    pub fn insert(&mut self, word: &str) {
        let mut node = &mut self.root;

        for c in word.chars() {
            node = node.children.entry(c).or_default();
        }
        node.is_end_of_word = true;
    }

    pub fn contains(&self, word: &str) -> bool {
        let mut node = &self.root;

        for c in word.chars() {
            match node.children.get(&c) {
                Some(child) => node = child,
                None => return false,
            }
        }

        node.is_end_of_word
    }
}
