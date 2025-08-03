def count_words_in_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            words = content.split()
            word_count = len(words)
            print(f"✅ Total number of words in '{filename}': {word_count}")
    except FileNotFoundError:
        print(f"❌ Error: File '{filename}' not found.")
    except Exception as e:
        print(f"⚠️ An unexpected error occurred: {e}")

# Driver code
if __name__ == "__main__":
    print("📄 Word Counter Program")
    filename = input("Enter the name of the text file (with extension): ")
    count_words_in_file(filename)
