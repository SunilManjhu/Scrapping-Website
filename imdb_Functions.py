# Send a GET request to the URL
from bs4 import BeautifulSoup
import requests
from logger import setup_logger

# Set up the logger
logger = setup_logger(log_file="imdb.log")

# ... (other imports and functions)
def get_url_data(url, user_agent):
    # Import required moduels for this funciton only

    # GET request and capture the response
    try:
        response = make_request_to_url(url=url, user_agent=user_agent)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")  #   print(soup)

        # Get-ListOfMovies
        moviesList = get_movie_list(soupData=soup)

        # Process-ListOfMovies
        Process_data(movie_list=moviesList)

    except requests.exceptions.RequestException as req_ex:
        print(f"ERROR: Request error - {req_ex}")
        logger.error(msg=f"ERROR: Request error - {req_ex}")
    except Exception as ex:
        logger.error(msg=f"ERROR: Request error - {ex}")
        print(f"ERROR: {ex}")


def make_request_to_url(url, user_agent):
    return requests.get(url=url, headers={"User-Agent": user_agent})


def get_movie_list(soupData):
    try:
        return soupData.find(
            name="ul",
            class_="ipc-metadata-list ipc-metadata-list--dividers-between sc-9d2f6de0-0 iMNUXk compact-list-view ipc-metadata-list--base",
        ).find_all(
            name="li",
            class_="ipc-metadata-list-summary-item sc-59b6048d-0 cuaJSp cli-parent",
        )  # print(len(movies))  # confirm the number of items matches the webpage
    except AttributeError as attr_Err:
        print(f"ERROR: Attribute error - {attr_Err}")
        logger.error(msg=f"ERROR: Attribute error - {attr_Err}")


def Process_data(movie_list):
    # Create a dictionary to store the values
    data_dict = {}

    # Go through the list
    for movie_item in movie_list:
        movie_data = extract_movie_data(movie_item)
        movie_data_other = extract_movie_data_Other(movie_item)

        result = combine_data(movie_data, movie_data_other)

        # Output to Console
        output_to_console(result)


def extract_movie_data(movieItem):
    try:
        return (
            movieItem.find(
                "div",
                class_="ipc-title ipc-title--base ipc-title--title ipc-title-link-no-icon ipc-title--on-textPrimary sc-479faa3c-9 dkLVoC cli-title",
            )
            .get_text(strip=True)
            .split(".")
        )
    except AttributeError as attr_Err:
        print(f"ERROR: Attribute error - {attr_Err}")
        logger.error(msg=f"ERROR: Attribute error - {attr_Err}")


def extract_movie_data_Other(movieItem):
    try:
        return movieItem.find(
            "div",
            class_="sc-479faa3c-7 jXgjdT cli-title-metadata",
        )
    except AttributeError as attr_Err:
        print(f"ERROR: Attribute error - {attr_Err}")
        logger.error(msg=f"ERROR: Attribute error - {attr_Err}")


def combine_data(movie_data, movie_data_other):
    keys_for_movie_data = ["RankOfMovie", "TitleOfMovie"]
    keys_for_movie_data_other = ["DateOfMoive", "LenthOfMoive", "CategoryOfMoive"]

    data_dict = dict(
        zip(
            keys_for_movie_data,
            (item.strip() for item in movie_data),
        )
    )
    data_dict.update(
        dict(
            zip(
                keys_for_movie_data_other,
                (span.get_text(strip=True) for span in movie_data_other),
            )
        )
    )

    return data_dict


def Output_Console_Style1(data_dict):
    print(data_dict)


def Output_Console_Style2(data_dict):
    for _ in data_dict:
        print(_, " : ", data_dict[_])
        break
    print("\n")


def output_to_console(data_dict, style=1):
    # CSV style     -   style 1
    # Text style    -   style 2
    if style == 1:
        print(data_dict)
    else:
        for key, value in data_dict.items():
            print(f"{key} : {value}")
        print("\n")

if __name__ == "__main__":
    # If this module is run as a standalone script, configure the logger
    setup_logger(log_file="imdb.log")
