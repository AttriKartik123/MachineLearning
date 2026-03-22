def medical_data_transformer(raw_text, window_size=512, overlap=50):
    """
    Transforms long medical text into overlapping semantic windows
    to ensure no symptoms are missed at the boundaries.
    """
    # Step 1: Clean and split the raw medical input into individual words
    words = raw_text.split()
    chunks = []
    
    # Step 2: Create overlapping windows (sliding window algorithm)
    # This prevents 'Semantic Loss' at the end of a chunk
    for i in range(0, len(words), window_size - overlap):
        chunk = " ".join(words[i : i + window_size])
        chunks.append(chunk)
        
        # Stop if we've reached the end of the text
        if i + window_size >= len(words):
            break

    # Step 3: Return structured payload for the Medical Transformer Core
    return {
        "total_segments": len(chunks),
        "payload": chunks,
        "metadata": {
            "window_size": window_size,
            "stride": window_size - overlap,
            "context_overlap": overlap
        }
    }

# Example Usage for your VitalNav Dashboard:
# user_input = "Patient describes chronic chest pain and shortness of breath..."
# processed_data = medical_data_transformer(user_input)