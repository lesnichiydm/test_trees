from copy import deepcopy
from treelib import Tree, Node


class TreeStore:
    def __init__(self, ts_list):
        self._ts_list = ts_list
        self.tree = self._create_tree()

    def _create_tree(self):
        tree = Tree()
        try:
            root = list(filter(
                lambda x: x["parent"] == "root",
                self._ts_list,
            ))[0]
        except IndexError:
            raise Exception("Root node not found")
        # add root
        tree.create_node(root["id"], root["id"], data=root)
        # add all items to tree
        for i in self._ts_list:
            if i["parent"] == "root":
                continue
            tree.create_node(
                i["id"],
                i["id"],
                parent=root["id"],
                data=i,
            )
        # move node by parent
        for node in tree.all_nodes_itr():
            if node.is_root():
                continue
            tree.move_node(
                node.identifier,
                node.data["parent"],
            )
        return tree

    def get_all(self):
        return self._ts_list

    def show(self):
        self.tree.show()

    def get_item(self, item_id):
        return self.tree.get_node(item_id).data

    def get_children(self, item_id):
        return [
            self.tree.get_node(i).data for i in self.tree.is_branch(item_id)
        ]

    def get_all_parents(self, item_id):
        all_parents = []
        while True:
            node = self.tree.parent(item_id)
            all_parents.append(node.data)
            if node.is_root():
                break
            item_id = node.identifier
        return all_parents
