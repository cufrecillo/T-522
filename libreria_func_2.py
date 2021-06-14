bookshop = [{
    "id": "cf_1",
    "title": "El hombre bicentenario",
    "author": "Isaac Asimov",
    "genre": "Ciencia ficción"
},
{
    "id": "ne_1",
    "title": "Lobo de mar",
    "author": "Jackc ALondon",
    "genre": "Narrativa extranjera"
},
{
    "id": "np_1",
    "title": "El legado de los huesos",
    "author": "Dolores Redondo",
    "genre": "Narrativa policíaca"
},
{
    "id": "dc_1",
    "title": "El error de Descartes",
    "author": "Antonio Damasio",
    "genre": "Divulgación científica"
},
{
    "id": "dc_2",
    "title": "El ingenio de los pájaros",
    "author": "Jennifer Ackerman",
    "genre": "Divulgación científica"
},
{
    "id": "ne_2",
    "title": "El corazón de las tinieblas",
    "author": "Joseph Conrad",
    "genre": "Narrativa extranjera"
},
{
    "id": "dc_5",
    "title": "Metro 2033",
    "author": "Dmitri Glujovski",
    "genre": "Divulgación científica"
},
{
    "id": "dc_5",
    "title": "Sidharta",
    "author": "Hermann Hesse",
    "genre": "Narrativa extranjera"
},
{
    "id": "el_1",
    "title": "Andres Trapiello",
    "author": "Las armas y las letras",
    "genre": "Narrativa extranjera"
},
{
    "id": "aa_1",
    "title": "El poder del ahora",
    "author": "Ekhart Tolle",
    "genre": "Narrativa extranjera"
},
]



# id_book = "dc_1"

# for book in bookshop: 
#     if book["id"] == id_book:
#         print(book)

def menu():
    print("Bookshop".center(50, "-"))
    print("1. ID")
    print("2. Author")
    print("3. Title")
    print("4. Genre")
    print("5. New book")
    print("6. Modify book")
    print("7. Delete book")    
    print("Q. Exit")

def book_by_id(id_book, libreria):
    for book in libreria:
        if book["id"] == id_book:
            return book #break DEVOLVERÁ EL LIBRO APENAS ENCUENTRE UNA COINCIDENCIA

def books_by_key(search_term, libreria, key):
    result = []
    for book in libreria:
        if book[key].lower().find(search_term.lower()) >= 0:      
            result.append(book)
    return result

def create_book(genre, bookshop):
    new_book = {}
    keys = list(bookshop[0].keys())
    for key in keys[1:3]:
        new_book[key] = input(f"{key}: ")
    new_book[keys[3]] = genre

    genre = genre.lower()
    word_cut = genre.split(" ")
    if len(word_cut) == 1:
        book_id = f"{word_cut[0][0]}{word_cut[0][-1]}_{len(bookshop)}" # word_cut[0][0] + word_cut[0][-1] + "_" + len(bookshop)
    else:
        book_id = f"{word_cut[0][0]}{word_cut[1][0]}_{len(bookshop)}"
    new_book[keys[0]] = book_id
    bookshop.append(new_book)

def print_genres():
    for i, genre in enumerate(genres): 
            print(f"{i + 1 }. {genre}")

def print_pretty(book_to_print):
    for k, v in book_to_print.items():
            print(f"{k}: {v}")

user = "0"
while user != "q":
    genres = ["Narrativa extranjera", "Divulgación científica", "Narrativa policíaca", "Ciencia ficción", "Autoayuda"]
    menu()
    user = input("Choose: ")

    if user == "1": # OPCIÓN ID:
        user_id = input("id: ")
        book = book_by_id(user_id, bookshop)
        if book != None:
            print_pretty(book)
        else:
            print("Libro no encontrado")
                
    elif user == "2": # GET BY AUTHOR
        key = "author"
        user_author = input("author: ").lower()
        books_by_author = books_by_key(user_author, bookshop, key)
        for book in books_by_author:
            print_pretty(book)
            print("------------")


    elif user == "3": # GET BY TITLE
        user_title = input("Title: ").lower()
        books_by_title = books_by_key(user_title, bookshop, "title")
        for book in books_by_title:
            print_pretty(book)
            print("------------")
        

    elif user == "4": # GET BY GENRE
        key = "genre"
        for i, genre in enumerate(genres): 
            print(f"{i + 1 }. {genre}")
        # print_genres()
        user_index = int(input("Choose: "))
        user_genre = genres[user_index - 1]
        result = books_by_key(user_genre, bookshop, key)        
        print(f"{user_genre}".center(50,"-"))

        for book in result:
            print_pretty(book)
            input("Continue...")
            print("".center(50,"-"))
        print(f"Se han encontrado {len(result)} libros.")

    elif user == "5":  # CREATE BOOK
        print_genres()
        user = int(input("Choose: ")) - 1
        user_genre = genres[user]    
        create_book(user_genre,bookshop)

    elif user == "6": # UPDATE BOOK
        book_id = input("ID: ") # dc_1
        book_to_update = book_by_id(book_id, bookshop)
        if book_to_update == None:
            print(f"El id: {book_id}, no se encuentra en nuestra base de datos.")
        else:
            keys = list(book_to_update)
            for i, key in enumerate(keys):
                print(f"{i + 1}. {key}")
            user = int(input("Choose: ")) - 1
            key = keys[user]
            bookshop.remove(book_to_update)
            book_to_update[key] = input("Nuevo valor: ")
            bookshop.append(book_to_update)

    elif user == "7": # DELETE BOOK
        book_id = input("ID: ")
        for book in bookshop:
            if book["id"] == book_id:
                for k, v in book.items(): # IMPRIMIR LAS SPECS DEL LIBRO
                    print(f"{k}: {v}")
                user = input(f"The book {book['title']} will be erase from the db. Are you sure (Y/N)?: ")
                if user.lower() == "y":
                    bookshop.remove(book)
                    print("The book was erased")

    elif user == "7": # DELETE BOOK TERCER ALTERNATIVA CON BOOK_BY_ID + I (indice)
        user = input("id: ")
        book_to_delete = book_by_id(user)
        user = input("Está seguro que desea eliminar el libro (y/n): ").lower()
        if user == "y":
            bookshop.remove(book_to_delete)
                      

    elif user.lower() == "q":
        user = user.lower()
        print("Bye!")
    else:
        user = "1"
        

