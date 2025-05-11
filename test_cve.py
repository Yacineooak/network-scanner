from cve_checker import CVEChecker

checker = CVEChecker()
checker.search_cve("smb")  # Tu peux changer "smb" par "http", "ftp", "ssh"...
