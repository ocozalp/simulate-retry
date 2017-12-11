from impl.timeline import Timeline


class TimeIntervals(Timeline):

    class Node:
        def __init__(self, start, end, val):
            self.start = start
            self.end = end
            self.val = val
            self.next_node = None

    def __init__(self, max_value):
        super(TimeIntervals, self).__init__(max_value)
        self.head = TimeIntervals.Node(1, max_value, 0)

    def get(self, index):
        if index > self.max_value or 0 > index:
            raise Exception('Index (%d) out of bounds' % index)

        current = self.head
        while current is not None:
            if current.start <= index <= current.end:
                return current.val
            current = current.next_node

        raise Exception('Unexpected state in get()')

    def inc(self, start, end, d):
        parent = None
        current = self.head
        current_start = start
        while current is not None:
            next_node = current.next_node

            if current.end >= current_start:
                new_nodes = self.__divide_node(current, current_start, end, d)

                if parent is not None:
                    parent.next_node = new_nodes[0]
                else:
                    self.head = new_nodes[0]

                new_nodes[-1].next_node = next_node
                current = new_nodes[-1]
                current_start = current.end + 1
            elif current.start > end:
                break

            parent = current
            current = next_node

        self.__defrag()

    def __defrag(self):
        current = self.head
        parent = None
        while current is not None:
            next_node = current.next_node
            end_node = current
            while next_node is not None:
                if next_node.val == current.val:
                    end_node = next_node
                    next_node = next_node.next_node
                else:
                    break

            if end_node is not None and end_node != current:
                current = self.__merge(current, end_node)
                if parent is not None:
                    parent.next_node = current
                else:
                    self.head = current
                next_node = current.next_node

            parent = current
            current = next_node

    def __merge(self, node1, node2):
        result = TimeIntervals.Node(node1.start, node2.end, node1.val)
        result.next_node = node2.next_node
        return result

    def __divide_node(self, node, start, end, d):
        result = list()
        if start > node.start:
            result.append(TimeIntervals.Node(node.start, start - 1, node.val))

        result.append(TimeIntervals.Node(start, min(end, node.end), node.val + d))

        if end < node.end:
            result.append(TimeIntervals.Node(end + 1, node.end, node.val))

        for i in xrange(1, len(result)):
            result[i-1].next_node = result[i]

        return result
