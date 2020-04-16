import math
import KNNCluster.ClusterHead as Head
import Objects.prediction as Prediction


def get_clusters(predictions, enemies):
    clusters = []
    N = len(predictions)
    K = int(math.sqrt(N))

    heads = []
    for i in range(0, 9):
        heads.append(Head.ClusterHead(i))

    while True:

        for prediction in predictions:
            nearest_head = 0
            min_dist = 300
            i = 0
            for head in heads:
                dist = head.get_distance(prediction)
                if dist < min_dist:
                    min_dist = dist
                    nearest_head = i

                i = i + 1

            heads[nearest_head].add_child(prediction)

        max_delta = 0
        for head in heads:
            delta = head.update_position()
            if delta > max_delta:
                max_delta = delta

        if max_delta < 0.1:
            break

        else:
            for head in heads:
                head.reset()

    print("Value of K is " + str(K))
    for head in heads:
        print("For cluster " + str(head.get_id()) + "we have " + str(head.get_child_count()) + " children and nearest enemy is at distance of " + str(head.get_nearest_enemy_dist(enemies)) + " meters")

    for head in heads:
        if head.get_child_count() > 0:
            clusters.append(Prediction.Prediction(head.get_position()[1], head.get_position()[0]))

    return clusters
