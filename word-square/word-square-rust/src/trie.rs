#[derive(Clone)]
pub struct TrieNode {
    pub children: Vec<Option<Box<TrieNode>>>,
    pub is_end_of_word: bool,
}

impl TrieNode {
    pub fn new() -> Self {
        Self {
            children: vec![None; 26],
            is_end_of_word: false,
        }
    }
}

#[allow(dead_code)]
pub struct Trie {
    pub root: TrieNode,
}

impl Trie {
    pub fn new() -> Self {
        Self {
            root: TrieNode::new(),
        }
    }

    pub fn char_index(c: char) -> usize {
        (c as u32 - 97) as usize
    }

    pub fn insert(&mut self, word: &str) {
        let mut node = &mut self.root;
        for c in word.chars() {
            let index = Self::char_index(c);
            node = node.children[index].get_or_insert_with(|| Box::new(TrieNode::new()));
        }
        node.is_end_of_word = true;
    }

    pub fn contains(&self, word: &str) -> bool {
        let mut node = &self.root;

        for c in word.chars() {
            let index = Self::char_index(c);
            match &node.children[index] {
                Some(child) => node = child,
                None => return false,
            }
        }

        node.is_end_of_word
    }
}
