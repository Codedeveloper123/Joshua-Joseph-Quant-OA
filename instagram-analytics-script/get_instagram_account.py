from defines import getCreds, makeApiCall


def getInstagramAccount(params):
    """Get instagram account

    API Endpoint:
            https://graph.facebook.com/{graph-api-version}/{page-id}?access_token={your-access-token}&fields=instagram_business_account
    Returns:
            object: data from the endpoint
    """
    endpointParams = dict()  # parameter to send to the endpoint
    endpointParams["access_token"] = params[
        "page_access_token"
    ]  # tell facebook we want to exchange token
    endpointParams["fields"] = "instagram_business_account "  # access token
    url = params["endpoint_base"] + params["page_id"]  # endpoint url
    return makeApiCall(url, endpointParams, params["debug"])  # make the api call


params = getCreds()
params["debug"] = "yes"
response = getInstagramAccount(params)
print("\n---- INSTAGRAM ACCOUNT INFO ----\n")
print("Page Id:")  # label
print(response["json_data"]["id"])  # display the page id
print("\nInstagram Account Id:")  # label
print(
    response["json_data"]["instagram_business_account"]["id"]
)  # display the instagram account id
