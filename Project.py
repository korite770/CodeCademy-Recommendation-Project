# make a recomemendation on books based on user preference by genres , e.g. fiction, non-fiction, mystery, etc. The program will recommend specific books by title according to their genres

from books_dataset import load_data, get_titles_by_genre
data = load_data()
# prompt user to get their preferred genre
user_genre = input("Enter your preferred book genre (e.g., Fiction, Mystery, Science Fiction): ")
print(f"Books in the genre '{user_genre}':")
titles = get_titles_by_genre(user_genre)
# if user you pick a certain genre, list all the titles in that genre
if titles:
    for title in titles:
        print(' = ', title)
else:
    print("No books found in this genre.")