from collections import deque

def compile_complete_graph(G, lexemes):
    """This instantiates the graph with the complete set of lexeme relationships"""
    for word, lex in lexemes.items():
        lex.prune()

        # skip empty nodes
        if not lex.next:
            continue

        print("%s: %s" % (word, lex.next))
        G.add_node(word, next=str(lex.next), prev=str(lex.prev))
        for next_word, count in lex.next.items():
            G.add_node(next_word)
            G.add_edge(word, next_word, weight=count)

def compile_from_start(G, lexemes, start):
    print(lexemes)
    print(start)
    print(lexemes[start])
    lex = lexemes[start]
    lex.prune()
    visited = set()
    visited.add(lex)
    print("%s: %s" % (lex.value, lex.next))

    next_lexemes = deque([(lex, lexemes[k]) for k, _ in lex.next.items()])

    while next_lexemes:
        og, lex = next_lexemes.popleft()
        lex.prune()
        print("%s: %s" % (lex.value, lex.next))

        visited.add(lex)
        for k, _ in lex.next.items():
            l = lexemes[k]
            if l not in visited and l not in next_lexemes:
                next_lexemes.append((lex, l))
        
        G.add_node(lex.value)
        G.add_edge(og.value, lex.value, weight=og.next[lex.value])
