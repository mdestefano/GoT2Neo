function* range(start, end) {
    yield start;
    if (start === end) return;
    yield* range(start + 1, end);
}