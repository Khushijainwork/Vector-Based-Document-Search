{"payload":{"allShortcutsEnabled":true,"fileTree":{"":{"items":[{"name":"CM1208testcases(5)","path":"CM1208testcases(5)","contentType":"directory"},{"name":"DocSearch.py","path":"DocSearch.py","contentType":"file"},{"name":"README.md","path":"README.md","contentType":"file"}],"totalCount":3}},"fileTreeProcessingTime":10.850124,"foldersToFetch":[],"repo":{"id":615923227,"defaultBranch":"main","name":"Document-Search-Python-","ownerLogin":"Khushijain30","currentUserCanPush":true,"isFork":false,"isEmpty":false,"createdAt":"2023-03-19T09:52:01.000+05:30","ownerAvatar":"https://avatars.githubusercontent.com/u/125923783?v=4","public":true,"private":false,"isOrgOwned":false},"symbolsExpanded":false,"treeExpanded":true,"refInfo":{"name":"main","listCacheKey":"v0:1679200017.0","canEdit":true,"refType":"branch","currentOid":"75fe494e2d86a19479693f5f1a9297f61df72589"},"path":"DocSearch.py","currentUser":{"id":125923783,"login":"Khushijain30","userEmail":"jainkhushi640.kj@gmail.com"},"blob":{"rawLines":["import math","","def dotProd(v1, v2):","    return sum((a*b) for a, b in zip(v1, v2))","","def L(v):","    return math.sqrt(dotProd(v, v))","","def angle(v1, v2):","    return (180/math.pi)*math.acos(dotProd(v1, v2) / (L(v1) * L(v2)))","","with open(\"docs.txt\", \"r\") as f:","    docs = []","    for line in f.readlines():","        line = line.strip()","        lineModified = line.maketrans(\"\\t\", \" \")","        docs.append(line.translate(lineModified))","","vocab = []","invertedIndex = {}","for id, doc in enumerate(docs):","    for word in doc.split(\" \"):","        if word not in vocab:","            vocab.append(word)","            invertedIndex[word] = [id+1]","        else:","            if (id+1) not in invertedIndex[word]:","                invertedIndex[word].append(id+1)","","docVector = [[0 for i in range(len(vocab))] for j in range(len(docs))]","for id, doc in enumerate(docs):","    for word in doc.split(\" \"):","        docVector[id][vocab.index(word)] += 1","","print(\"Words in dictionary: \",len(vocab))","with open(\"queries.txt\", \"r\") as f:","    for line in f.readlines():","        query = line.strip()","        print(\"Query: \", query)","        relevantDocuments = []","        queryVector = [0 for i in range(len(vocab))]","        for word in query.split(\" \"):","            if word in invertedIndex:","                queryVector[vocab.index(word)] = 1","                relevantDocuments.append(invertedIndex[word])","        result = list(set.intersection(*map(set,relevantDocuments)))","        print(\"Relevant documents:\", \" \".join(str(x) for x in result))","        if len(result)!=0:","            search = []","            for docId in result:","                search.append((docId, angle(docVector[docId-1], queryVector)))","            sortedSearch = sorted(search, key=lambda x: x[1])","            for docId, angleVectors in sortedSearch:","                print(\"{0:d} {1:.2f}\".format(docId, angleVectors))"],"stylingDirectives":[[{"start":0,"end":6,"cssClass":"pl-k"},{"start":7,"end":11,"cssClass":"pl-s1"}],[],[{"start":0,"end":3,"cssClass":"pl-k"},{"start":4,"end":11,"cssClass":"pl-en"},{"start":12,"end":14,"cssClass":"pl-s1"},{"start":16,"end":18,"cssClass":"pl-s1"}],[{"start":4,"end":10,"cssClass":"pl-k"},{"start":11,"end":14,"cssClass":"pl-en"},{"start":16,"end":17,"cssClass":"pl-s1"},{"start":17,"end":18,"cssClass":"pl-c1"},{"start":18,"end":19,"cssClass":"pl-s1"},{"start":21,"end":24,"cssClass":"pl-k"},{"start":25,"end":26,"cssClass":"pl-s1"},{"start":28,"end":29,"cssClass":"pl-s1"},{"start":30,"end":32,"cssClass":"pl-c1"},{"start":33,"end":36,"cssClass":"pl-en"},{"start":37,"end":39,"cssClass":"pl-s1"},{"start":41,"end":43,"cssClass":"pl-s1"}],[],[{"start":0,"end":3,"cssClass":"pl-k"},{"start":4,"end":5,"cssClass":"pl-v"},{"start":6,"end":7,"cssClass":"pl-s1"}],[{"start":4,"end":10,"cssClass":"pl-k"},{"start":11,"end":15,"cssClass":"pl-s1"},{"start":16,"end":20,"cssClass":"pl-en"},{"start":21,"end":28,"cssClass":"pl-en"},{"start":29,"end":30,"cssClass":"pl-s1"},{"start":32,"end":33,"cssClass":"pl-s1"}],[],[{"start":0,"end":3,"cssClass":"pl-k"},{"start":4,"end":9,"cssClass":"pl-en"},{"start":10,"end":12,"cssClass":"pl-s1"},{"start":14,"end":16,"cssClass":"pl-s1"}],[{"start":4,"end":10,"cssClass":"pl-k"},{"start":12,"end":15,"cssClass":"pl-c1"},{"start":15,"end":16,"cssClass":"pl-c1"},{"start":16,"end":20,"cssClass":"pl-s1"},{"start":21,"end":23,"cssClass":"pl-s1"},{"start":24,"end":25,"cssClass":"pl-c1"},{"start":25,"end":29,"cssClass":"pl-s1"},{"start":30,"end":34,"cssClass":"pl-en"},{"start":35,"end":42,"cssClass":"pl-en"},{"start":43,"end":45,"cssClass":"pl-s1"},{"start":47,"end":49,"cssClass":"pl-s1"},{"start":51,"end":52,"cssClass":"pl-c1"},{"start":54,"end":55,"cssClass":"pl-v"},{"start":56,"end":58,"cssClass":"pl-s1"},{"start":60,"end":61,"cssClass":"pl-c1"},{"start":62,"end":63,"cssClass":"pl-v"},{"start":64,"end":66,"cssClass":"pl-s1"}],[],[{"start":0,"end":4,"cssClass":"pl-k"},{"start":5,"end":9,"cssClass":"pl-en"},{"start":10,"end":20,"cssClass":"pl-s"},{"start":22,"end":25,"cssClass":"pl-s"},{"start":27,"end":29,"cssClass":"pl-k"},{"start":30,"end":31,"cssClass":"pl-s1"}],[{"start":4,"end":8,"cssClass":"pl-s1"},{"start":9,"end":10,"cssClass":"pl-c1"}],[{"start":4,"end":7,"cssClass":"pl-k"},{"start":8,"end":12,"cssClass":"pl-s1"},{"start":13,"end":15,"cssClass":"pl-c1"},{"start":16,"end":17,"cssClass":"pl-s1"},{"start":18,"end":27,"cssClass":"pl-en"}],[{"start":8,"end":12,"cssClass":"pl-s1"},{"start":13,"end":14,"cssClass":"pl-c1"},{"start":15,"end":19,"cssClass":"pl-s1"},{"start":20,"end":25,"cssClass":"pl-en"}],[{"start":8,"end":20,"cssClass":"pl-s1"},{"start":21,"end":22,"cssClass":"pl-c1"},{"start":23,"end":27,"cssClass":"pl-s1"},{"start":28,"end":37,"cssClass":"pl-en"},{"start":38,"end":42,"cssClass":"pl-s"},{"start":39,"end":41,"cssClass":"pl-cce"},{"start":44,"end":47,"cssClass":"pl-s"}],[{"start":8,"end":12,"cssClass":"pl-s1"},{"start":13,"end":19,"cssClass":"pl-en"},{"start":20,"end":24,"cssClass":"pl-s1"},{"start":25,"end":34,"cssClass":"pl-en"},{"start":35,"end":47,"cssClass":"pl-s1"}],[],[{"start":0,"end":5,"cssClass":"pl-s1"},{"start":6,"end":7,"cssClass":"pl-c1"}],[{"start":0,"end":13,"cssClass":"pl-s1"},{"start":14,"end":15,"cssClass":"pl-c1"}],[{"start":0,"end":3,"cssClass":"pl-k"},{"start":4,"end":6,"cssClass":"pl-s1"},{"start":8,"end":11,"cssClass":"pl-s1"},{"start":12,"end":14,"cssClass":"pl-c1"},{"start":15,"end":24,"cssClass":"pl-en"},{"start":25,"end":29,"cssClass":"pl-s1"}],[{"start":4,"end":7,"cssClass":"pl-k"},{"start":8,"end":12,"cssClass":"pl-s1"},{"start":13,"end":15,"cssClass":"pl-c1"},{"start":16,"end":19,"cssClass":"pl-s1"},{"start":20,"end":25,"cssClass":"pl-en"},{"start":26,"end":29,"cssClass":"pl-s"}],[{"start":8,"end":10,"cssClass":"pl-k"},{"start":11,"end":15,"cssClass":"pl-s1"},{"start":16,"end":19,"cssClass":"pl-c1"},{"start":20,"end":22,"cssClass":"pl-c1"},{"start":23,"end":28,"cssClass":"pl-s1"}],[{"start":12,"end":17,"cssClass":"pl-s1"},{"start":18,"end":24,"cssClass":"pl-en"},{"start":25,"end":29,"cssClass":"pl-s1"}],[{"start":12,"end":25,"cssClass":"pl-s1"},{"start":26,"end":30,"cssClass":"pl-s1"},{"start":32,"end":33,"cssClass":"pl-c1"},{"start":35,"end":37,"cssClass":"pl-s1"},{"start":37,"end":38,"cssClass":"pl-c1"},{"start":38,"end":39,"cssClass":"pl-c1"}],[{"start":8,"end":12,"cssClass":"pl-k"}],[{"start":12,"end":14,"cssClass":"pl-k"},{"start":16,"end":18,"cssClass":"pl-s1"},{"start":18,"end":19,"cssClass":"pl-c1"},{"start":19,"end":20,"cssClass":"pl-c1"},{"start":22,"end":25,"cssClass":"pl-c1"},{"start":26,"end":28,"cssClass":"pl-c1"},{"start":29,"end":42,"cssClass":"pl-s1"},{"start":43,"end":47,"cssClass":"pl-s1"}],[{"start":16,"end":29,"cssClass":"pl-s1"},{"start":30,"end":34,"cssClass":"pl-s1"},{"start":36,"end":42,"cssClass":"pl-en"},{"start":43,"end":45,"cssClass":"pl-s1"},{"start":45,"end":46,"cssClass":"pl-c1"},{"start":46,"end":47,"cssClass":"pl-c1"}],[],[{"start":0,"end":9,"cssClass":"pl-s1"},{"start":10,"end":11,"cssClass":"pl-c1"},{"start":14,"end":15,"cssClass":"pl-c1"},{"start":16,"end":19,"cssClass":"pl-k"},{"start":20,"end":21,"cssClass":"pl-s1"},{"start":22,"end":24,"cssClass":"pl-c1"},{"start":25,"end":30,"cssClass":"pl-en"},{"start":31,"end":34,"cssClass":"pl-en"},{"start":35,"end":40,"cssClass":"pl-s1"},{"start":44,"end":47,"cssClass":"pl-k"},{"start":48,"end":49,"cssClass":"pl-s1"},{"start":50,"end":52,"cssClass":"pl-c1"},{"start":53,"end":58,"cssClass":"pl-en"},{"start":59,"end":62,"cssClass":"pl-en"},{"start":63,"end":67,"cssClass":"pl-s1"}],[{"start":0,"end":3,"cssClass":"pl-k"},{"start":4,"end":6,"cssClass":"pl-s1"},{"start":8,"end":11,"cssClass":"pl-s1"},{"start":12,"end":14,"cssClass":"pl-c1"},{"start":15,"end":24,"cssClass":"pl-en"},{"start":25,"end":29,"cssClass":"pl-s1"}],[{"start":4,"end":7,"cssClass":"pl-k"},{"start":8,"end":12,"cssClass":"pl-s1"},{"start":13,"end":15,"cssClass":"pl-c1"},{"start":16,"end":19,"cssClass":"pl-s1"},{"start":20,"end":25,"cssClass":"pl-en"},{"start":26,"end":29,"cssClass":"pl-s"}],[{"start":8,"end":17,"cssClass":"pl-s1"},{"start":18,"end":20,"cssClass":"pl-s1"},{"start":22,"end":27,"cssClass":"pl-s1"},{"start":28,"end":33,"cssClass":"pl-en"},{"start":34,"end":38,"cssClass":"pl-s1"},{"start":41,"end":43,"cssClass":"pl-c1"},{"start":44,"end":45,"cssClass":"pl-c1"}],[],[{"start":0,"end":5,"cssClass":"pl-en"},{"start":6,"end":29,"cssClass":"pl-s"},{"start":30,"end":33,"cssClass":"pl-en"},{"start":34,"end":39,"cssClass":"pl-s1"}],[{"start":0,"end":4,"cssClass":"pl-k"},{"start":5,"end":9,"cssClass":"pl-en"},{"start":10,"end":23,"cssClass":"pl-s"},{"start":25,"end":28,"cssClass":"pl-s"},{"start":30,"end":32,"cssClass":"pl-k"},{"start":33,"end":34,"cssClass":"pl-s1"}],[{"start":4,"end":7,"cssClass":"pl-k"},{"start":8,"end":12,"cssClass":"pl-s1"},{"start":13,"end":15,"cssClass":"pl-c1"},{"start":16,"end":17,"cssClass":"pl-s1"},{"start":18,"end":27,"cssClass":"pl-en"}],[{"start":8,"end":13,"cssClass":"pl-s1"},{"start":14,"end":15,"cssClass":"pl-c1"},{"start":16,"end":20,"cssClass":"pl-s1"},{"start":21,"end":26,"cssClass":"pl-en"}],[{"start":8,"end":13,"cssClass":"pl-en"},{"start":14,"end":23,"cssClass":"pl-s"},{"start":25,"end":30,"cssClass":"pl-s1"}],[{"start":8,"end":25,"cssClass":"pl-s1"},{"start":26,"end":27,"cssClass":"pl-c1"}],[{"start":8,"end":19,"cssClass":"pl-s1"},{"start":20,"end":21,"cssClass":"pl-c1"},{"start":23,"end":24,"cssClass":"pl-c1"},{"start":25,"end":28,"cssClass":"pl-k"},{"start":29,"end":30,"cssClass":"pl-s1"},{"start":31,"end":33,"cssClass":"pl-c1"},{"start":34,"end":39,"cssClass":"pl-en"},{"start":40,"end":43,"cssClass":"pl-en"},{"start":44,"end":49,"cssClass":"pl-s1"}],[{"start":8,"end":11,"cssClass":"pl-k"},{"start":12,"end":16,"cssClass":"pl-s1"},{"start":17,"end":19,"cssClass":"pl-c1"},{"start":20,"end":25,"cssClass":"pl-s1"},{"start":26,"end":31,"cssClass":"pl-en"},{"start":32,"end":35,"cssClass":"pl-s"}],[{"start":12,"end":14,"cssClass":"pl-k"},{"start":15,"end":19,"cssClass":"pl-s1"},{"start":20,"end":22,"cssClass":"pl-c1"},{"start":23,"end":36,"cssClass":"pl-s1"}],[{"start":16,"end":27,"cssClass":"pl-s1"},{"start":28,"end":33,"cssClass":"pl-s1"},{"start":34,"end":39,"cssClass":"pl-en"},{"start":40,"end":44,"cssClass":"pl-s1"},{"start":47,"end":48,"cssClass":"pl-c1"},{"start":49,"end":50,"cssClass":"pl-c1"}],[{"start":16,"end":33,"cssClass":"pl-s1"},{"start":34,"end":40,"cssClass":"pl-en"},{"start":41,"end":54,"cssClass":"pl-s1"},{"start":55,"end":59,"cssClass":"pl-s1"}],[{"start":8,"end":14,"cssClass":"pl-s1"},{"start":15,"end":16,"cssClass":"pl-c1"},{"start":17,"end":21,"cssClass":"pl-en"},{"start":22,"end":25,"cssClass":"pl-s1"},{"start":26,"end":38,"cssClass":"pl-en"},{"start":39,"end":40,"cssClass":"pl-c1"},{"start":40,"end":43,"cssClass":"pl-en"},{"start":44,"end":47,"cssClass":"pl-s1"},{"start":48,"end":65,"cssClass":"pl-s1"}],[{"start":8,"end":13,"cssClass":"pl-en"},{"start":14,"end":35,"cssClass":"pl-s"},{"start":37,"end":40,"cssClass":"pl-s"},{"start":41,"end":45,"cssClass":"pl-en"},{"start":46,"end":49,"cssClass":"pl-en"},{"start":50,"end":51,"cssClass":"pl-s1"},{"start":53,"end":56,"cssClass":"pl-k"},{"start":57,"end":58,"cssClass":"pl-s1"},{"start":59,"end":61,"cssClass":"pl-c1"},{"start":62,"end":68,"cssClass":"pl-s1"}],[{"start":8,"end":10,"cssClass":"pl-k"},{"start":11,"end":14,"cssClass":"pl-en"},{"start":15,"end":21,"cssClass":"pl-s1"},{"start":22,"end":24,"cssClass":"pl-c1"},{"start":24,"end":25,"cssClass":"pl-c1"}],[{"start":12,"end":18,"cssClass":"pl-s1"},{"start":19,"end":20,"cssClass":"pl-c1"}],[{"start":12,"end":15,"cssClass":"pl-k"},{"start":16,"end":21,"cssClass":"pl-s1"},{"start":22,"end":24,"cssClass":"pl-c1"},{"start":25,"end":31,"cssClass":"pl-s1"}],[{"start":16,"end":22,"cssClass":"pl-s1"},{"start":23,"end":29,"cssClass":"pl-en"},{"start":31,"end":36,"cssClass":"pl-s1"},{"start":38,"end":43,"cssClass":"pl-en"},{"start":44,"end":53,"cssClass":"pl-s1"},{"start":54,"end":59,"cssClass":"pl-s1"},{"start":59,"end":60,"cssClass":"pl-c1"},{"start":60,"end":61,"cssClass":"pl-c1"},{"start":64,"end":75,"cssClass":"pl-s1"}],[{"start":12,"end":24,"cssClass":"pl-s1"},{"start":25,"end":26,"cssClass":"pl-c1"},{"start":27,"end":33,"cssClass":"pl-en"},{"start":34,"end":40,"cssClass":"pl-s1"},{"start":42,"end":45,"cssClass":"pl-s1"},{"start":45,"end":46,"cssClass":"pl-c1"},{"start":46,"end":52,"cssClass":"pl-k"},{"start":53,"end":54,"cssClass":"pl-s1"},{"start":56,"end":57,"cssClass":"pl-s1"},{"start":58,"end":59,"cssClass":"pl-c1"}],[{"start":12,"end":15,"cssClass":"pl-k"},{"start":16,"end":21,"cssClass":"pl-s1"},{"start":23,"end":35,"cssClass":"pl-s1"},{"start":36,"end":38,"cssClass":"pl-c1"},{"start":39,"end":51,"cssClass":"pl-s1"}],[{"start":16,"end":21,"cssClass":"pl-en"},{"start":22,"end":37,"cssClass":"pl-s"},{"start":38,"end":44,"cssClass":"pl-en"},{"start":45,"end":50,"cssClass":"pl-s1"},{"start":52,"end":64,"cssClass":"pl-s1"}]],"csv":null,"csvError":null,"dependabotInfo":{"showConfigurationBanner":null,"configFilePath":null,"networkDependabotPath":"/Khushijain30/Document-Search-Python-/network/updates","dismissConfigurationNoticePath":"/settings/dismiss-notice/dependabot_configuration_notice","configurationNoticeDismissed":false},"displayName":"DocSearch.py","displayUrl":"https://github.com/Khushijain30/Document-Search-Python-/blob/main/DocSearch.py?raw=true","headerInfo":{"blobSize":"1.8 KB","deleteTooltip":"Delete this file","editTooltip":"Edit this file","deleteInfo":{"deleteTooltip":"Delete this file"},"editInfo":{"editTooltip":"Edit this file"},"ghDesktopPath":"x-github-client://openRepo/https://github.com/Khushijain30/Document-Search-Python-?branch=main&filepath=DocSearch.py","isGitLfs":false,"gitLfsPath":null,"onBranch":true,"shortPath":"6ee17cb","siteNavLoginPath":"/login?return_to=https%3A%2F%2Fgithub.com%2FKhushijain30%2FDocument-Search-Python-%2Fblob%2Fmain%2FDocSearch.py","isCSV":false,"isRichtext":false,"toc":null,"lineInfo":{"truncatedLoc":"54","truncatedSloc":"47"},"mode":"file"},"image":false,"isCodeownersFile":null,"isPlain":false,"isValidLegacyIssueTemplate":false,"issueTemplateHelpUrl":"https://docs.github.com/articles/about-issue-and-pull-request-templates","issueTemplate":null,"discussionTemplate":null,"language":"Python","languageID":303,"large":false,"loggedIn":true,"planSupportInfo":{"repoIsFork":null,"repoOwnedByCurrentUser":null,"requestFullPath":"/Khushijain30/Document-Search-Python-/blob/main/DocSearch.py","showFreeOrgGatedFeatureMessage":null,"showPlanSupportBanner":null,"upgradeDataAttributes":null,"upgradePath":null},"publishBannersInfo":{"dismissActionNoticePath":"/settings/dismiss-notice/publish_action_from_dockerfile","releasePath":"/Khushijain30/Document-Search-Python-/releases/new?marketplace=true","showPublishActionBanner":false},"rawBlobUrl":"https://github.com/Khushijain30/Document-Search-Python-/raw/main/DocSearch.py","renderImageOrRaw":false,"richText":null,"renderedFileInfo":null,"shortPath":null,"symbolsEnabled":true,"tabSize":8,"topBannersInfo":{"overridingGlobalFundingFile":false,"globalPreferredFundingPath":null,"repoOwner":"Khushijain30","repoName":"Document-Search-Python-","showInvalidCitationWarning":false,"citationHelpUrl":"https://docs.github.com/github/creating-cloning-and-archiving-repositories/creating-a-repository-on-github/about-citation-files","actionsOnboardingTip":null},"truncated":false,"viewable":true,"workflowRedirectUrl":null,"symbols":{"timed_out":false,"not_analyzed":false,"symbols":[{"name":"dotProd","kind":"function","ident_start":17,"ident_end":24,"extent_start":13,"extent_end":79,"fully_qualified_name":"dotProd","ident_utf16":{"start":{"line_number":2,"utf16_col":4},"end":{"line_number":2,"utf16_col":11}},"extent_utf16":{"start":{"line_number":2,"utf16_col":0},"end":{"line_number":3,"utf16_col":45}}},{"name":"L","kind":"function","ident_start":85,"ident_end":86,"extent_start":81,"extent_end":126,"fully_qualified_name":"L","ident_utf16":{"start":{"line_number":5,"utf16_col":4},"end":{"line_number":5,"utf16_col":5}},"extent_utf16":{"start":{"line_number":5,"utf16_col":0},"end":{"line_number":6,"utf16_col":35}}},{"name":"angle","kind":"function","ident_start":132,"ident_end":137,"extent_start":128,"extent_end":216,"fully_qualified_name":"angle","ident_utf16":{"start":{"line_number":8,"utf16_col":4},"end":{"line_number":8,"utf16_col":9}},"extent_utf16":{"start":{"line_number":8,"utf16_col":0},"end":{"line_number":9,"utf16_col":69}}},{"name":"vocab","kind":"constant","ident_start":424,"ident_end":429,"extent_start":424,"extent_end":434,"fully_qualified_name":"vocab","ident_utf16":{"start":{"line_number":18,"utf16_col":0},"end":{"line_number":18,"utf16_col":5}},"extent_utf16":{"start":{"line_number":18,"utf16_col":0},"end":{"line_number":18,"utf16_col":10}}},{"name":"invertedIndex","kind":"constant","ident_start":435,"ident_end":448,"extent_start":435,"extent_end":453,"fully_qualified_name":"invertedIndex","ident_utf16":{"start":{"line_number":19,"utf16_col":0},"end":{"line_number":19,"utf16_col":13}},"extent_utf16":{"start":{"line_number":19,"utf16_col":0},"end":{"line_number":19,"utf16_col":18}}},{"name":"docVector","kind":"constant","ident_start":734,"ident_end":743,"extent_start":734,"extent_end":804,"fully_qualified_name":"docVector","ident_utf16":{"start":{"line_number":29,"utf16_col":0},"end":{"line_number":29,"utf16_col":9}},"extent_utf16":{"start":{"line_number":29,"utf16_col":0},"end":{"line_number":29,"utf16_col":70}}}]}},"copilotInfo":null,"copilotAccessAllowed":false,"csrf_tokens":{"/Khushijain30/Document-Search-Python-/branches":{"post":"a81lKg7rzLXIN7e8zO8Jx8xE1q5LB5y6_Nfz8urAeFBqKeUUz4EuMIG_75M_NLwdCK_BaMAUjRaV0X9WSO305A"},"/repos/preferences":{"post":"_2zC_LiI96nI9jaelXW9j2FoNptJ8x6apYy27QyYJZrZDvhi-2xF0NbRENxJRNSl626hE8cEyezrxhqeEFyi0w"}}},"title":"Document-Search-Python-/DocSearch.py at main · Khushijain30/Document-Search-Python-"}