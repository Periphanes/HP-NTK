import torch
import numpy as np

def prune_random(data):

    # print(data.edge_index[0][:100])
    # print(data.edge_index[1][:100])

    # print(torch.numel(torch.unique(data.edge_index[0])))
    # print(torch.numel(torch.unique(data.edge_index[1])))

    # print(np.max(data.edge_index[1].numpy()))
    # print(np.min(data.edge_index[1].numpy()))


    # k = data.edge_index[0] == 3658
    # k = k.nonzero()

    # print(data.edge_index[:, k])


    # exit(1)

    # torch.set_printoptions(profile="full")
    # print(torch.unique(data.edge_index[0]))
    # torch.set_printoptions(profile="default")

    random_indexes = torch.randperm(data.edge_index.shape[1])
    shuffled_edges = data.edge_index[:, random_indexes]

    # print(shuffled_edges.shape)

    prune_percent = 0.05

    edge_index_count = data.edge_index.shape[1]
    pruned_index_count = int(edge_index_count * prune_percent)

    prune_mask = torch.zeros((edge_index_count))
    prune_mask[pruned_index_count : ] = 1

    for k in range(pruned_index_count):
        p = shuffled_edges[1] == shuffled_edges[0][k].item()
        p = p.nonzero()
        p = [i.item() for i in p]

        q = shuffled_edges[0] == shuffled_edges[1][k].item()
        q = q.nonzero()
        q = [i.item() for i in q]

        index = -1

        print(p)
        print(q)
        exit(1)


    data.edge_index = shuffled_edges[:, pruned_index_count:]



    print(data.edge_index.shape)

    return data