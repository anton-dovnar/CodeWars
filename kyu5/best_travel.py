from itertools import combinations


def choose_best_sum(max_distance: int, visit_towns: int, distances: list):
    available_distances = sorted([sum(combination) for combination in combinations(distances, visit_towns)])
    if not available_distances:
        return None

    left, right = 0, len(available_distances) - 1
    while left <= right:
        mid = (left + right) // 2

        if max_distance == available_distances[mid]:
            return available_distances[mid]
        elif max_distance < available_distances[mid]:
            right = mid - 1
        else:
            left = mid + 1

    if available_distances[left-1] > max_distance and available_distances[right] > max_distance:
        return None
    else:
        return min(available_distances[left-1], available_distances[right])
