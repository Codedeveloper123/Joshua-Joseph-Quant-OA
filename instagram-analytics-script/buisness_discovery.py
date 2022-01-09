from defines import getCreds, makeApiCall


def getAccountInfo(params):
    """Get info on a users account

    API Endpoint:
            https://graph.facebook.com/{graph-api-version}/{ig-user-id}?fields=business_discovery.username({ig-username}){username,website,name,ig_id,id,profile_picture_url,biography,follows_count,followers_count,media_count}&access_token={access-token}
    Returns:
            object: data from the endpoint
    """
    endpointParams = dict()
    endpointParams["fields"] = (
        "business_discovery.username("
        + params["ig_username"]
        + "){username,website,name,ig_id,id,profile_picture_url,biography,follows_count,followers_count,media_count}"
    )
    endpointParams["access_token"] = params["access_token"]
    url = params["endpoint_base"] + params["instagram_account"]
    return makeApiCall(url, endpointParams, params["debug"])


"""
params = getCreds()
params["debug"] = ""
response = getAccountInfo(params)
print("\n---- ACCOUNT INFO -----\n")  # display latest post info
print("username:")  # label
print(response["json_data"]["business_discovery"]["username"])  # display username
print("\nnumber of posts:")  # label
print(
    response["json_data"]["business_discovery"]["media_count"]
)  # display number of posts user has made
print("\nfollowers:")  # label
print(
    response["json_data"]["business_discovery"]["followers_count"]
)  # display number of followers the user has
print("\nfollowing:")  # label
print(
    response["json_data"]["business_discovery"]["follows_count"]
)  # display number of people the user follows
print("\nprofile picture url:")  # label
print(
    response["json_data"]["business_discovery"]["profile_picture_url"]
)  # display profile picutre url
print("\nbiography:")  # label
print(
    response["json_data"]["business_discovery"]["biography"]
)  # display users about section
"""