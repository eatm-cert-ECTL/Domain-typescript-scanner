'''
Input: Domain name as string

Output: Domains as a list of string
'''
def generate(domain:str) -> list[str]:
    domainsOutputList = []
    for number in ['0','1','2','3','4','5','6','7','8','9']:
        domainsOutputList.append(domain+number)
    return domainsOutputList