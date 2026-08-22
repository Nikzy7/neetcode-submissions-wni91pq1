class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        valid_count = 0
        domains = defaultdict(list)

        for email in emails:
            mailing_address, domain = email.split("@")

            if not (domain.__contains__(".com") or domain.__contains__(".io")):
                continue

            mailing_address = mailing_address.split("+")[0]
            mailing_address = mailing_address.replace(".", "")

            if mailing_address not in domains.get(domain, []):
                domains[domain].append(mailing_address)
                valid_count += 1

        return valid_count
