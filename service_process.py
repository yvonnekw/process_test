def process_strings(input_strings):
    processed_strings = []

    for input_string in input_strings:
        if not input_string:
            # Skip empty input strings
            continue

        # Initialize variables to store processed string and previous character
        processed = ""
        prev_char = ""

        for char in input_string:
            if char == "$":
                # Replace dollar sign with pound sign
                processed += "£"
            elif char in ("_", "4"):
                # Remove underscores and the number 4
                continue
            else:
                # Check for contiguous duplicate characters
                if char.lower() != prev_char.lower():
                    processed += char
                prev_char = char

        # Truncate to a max length of 15 characters
        processed = processed[:15]

        processed_strings.append(processed)

    return processed_strings
