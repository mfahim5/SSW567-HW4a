import pip._vendor.requests
import json 

def githubAPI(username):
    
    try:
        result= pip._vendor.requests.get("https://api.github.com/users/" +username+"/repos")
    except (TypeError):
        return "Github account must be written correctly"

    result=result.json()
    if len(result)==0:
        print("No Repos")
        return False
    for i in result:
        resultRepo= pip._vendor.requests.get(i['commits_url'].split("{")[0])
        resultRepo= resultRepo.json()
        print("Repo Name: " + i['name']+"\t Number of commits: "+str(len(resultRepo)))
    return True

if __name__ == "__main__":
    response=input("Please put the Github Username: ")
    githubAPI(response)