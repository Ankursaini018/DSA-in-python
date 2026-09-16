def find_papers(papers, name):
    for paper in papers:
        if paper == name:
            return True
    return False

papers = ["paper1", "paper2", "paper3", "paper4", "paper5"]
search_name = "pap"
result = find_papers(papers, search_name)

if result:
    print("paper found")
else:
    print("not found")    