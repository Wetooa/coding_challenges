fn main() {
    let mut arr = vec![0; 100000];

    for i in 0..100000 {
        arr[i] = i;
    }

    for i in 0..100000 {
        println!("Value at index {}: {}", i, arr[i]);
    }
}
