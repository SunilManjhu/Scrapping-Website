# Send a GET request to the URL
from bs4 import BeautifulSoup


def get_url_data(url, user_agent):
    # Import required moduels for this funciton only

    # GET request and capture the response
    try:
        response = make_request_to_url(url=url, user_agent=user_agent)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")  #   print(soup)

        # Get-ListOfMovies
        moviesList = get_movie_list(soupData=soup)

        # Create a dictionary to store the values
        data_dict = {}

        for movieItem in moviesList:
            movieData = (
                movieItem.find(
                    "div",
                    class_="ipc-title ipc-title--base ipc-title--title ipc-title-link-no-icon ipc-title--on-textPrimary sc-479faa3c-9 dkLVoC cli-title",
                )
                .get_text(strip=True)
                .split(".")
            )

            # Define keys for the dictionary
            keys = ["RankOfMovie", "TitleOfMovie"]

            for key, item in zip(keys, movieData):
                data_dict[key] = item.strip()

            OtherInfoAboutMovie = movieItem.find(
                "div",
                class_="sc-479faa3c-7 jXgjdT cli-title-metadata",
            )

            # Define keys for the dictionary
            keys = ["DateOfMoive", "LenthOfMoive", "CategoryOfMoive"]

            for key, span in zip(keys, OtherInfoAboutMovie):
                # Get the text content of the span
                text_content = span.get_text(strip=True)
                data_dict[key] = text_content

            print(data_dict)

            # Uncomment to print on Console
            # for _ in data_dict:
            #     print(_," : ",data_dict[_])

            # print("\n")
            # # break

    except Exception as ex:
        print(f"ERROR: {ex}")


def make_request_to_url(url, user_agent):
    import requests

    # https://stackoverflow.com/questions/16627227/problem-http-error-403-in-python-3-web-scraping
    return requests.get(url=url, headers={"User-Agent": user_agent})


def get_movie_list(soupData):
    return soupData.find(
        name="ul",
        class_="ipc-metadata-list ipc-metadata-list--dividers-between sc-9d2f6de0-0 iMNUXk compact-list-view ipc-metadata-list--base",
    ).find_all(
        name="li",
        class_="ipc-metadata-list-summary-item sc-59b6048d-0 cuaJSp cli-parent",
    )  # print(len(movies))  # confirm the number of items matches the webpage

