import pygame
import random
import hashlib
import ipaddress
import sys

# Initialize Pygame
pygame.init()

# Window dimensions
WIDTH, HEIGHT = 1200, 650
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dynamic Network Visualization")

# Colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
<<<<<<< HEAD
RED = (255, 0, 0)
BLUE = (0,0,255)

# Parameters
node_size = 1000
view_size = 16
rounds = 100
attack_force = 1
k_rho = int(view_size//2)
rho = 0.5
=======
>>>>>>> 54e1dd7e43198161fcba31ac898ab186ff7ebe35

# Font for text
font = pygame.font.Font(None, 24)

def generate_random_ip():
    """Generate a random IP address for simulating a unique identifier."""
    return str(ipaddress.IPv4Address(random.getrandbits(32)))


def save_malicious_rates(file_path, counter, rate):
    with open(file_path, "w") as file:  # Utilisez le mode "a" pour ajouter à la fin du fichier
        file.write(f"{counter} : {rate}\n")

def save_malicious_rates_append(file_path, counter, rate):
    with open(file_path, "a") as file:  # Utilisez le mode "a" pour ajouter à la fin du fichier
        file.write(f"{counter} : {rate}\n")

class Node:
    def __init__(self, ip, x, y):
        self.ip = ip
        self.x = x
        self.y = y
        self.neighbors = []
        self.pull_list = []
        self.push_list = []
<<<<<<< HEAD
        self.seeds = [1]*view_size
        self.hits = [1]*view_size
        self.view_received = []
        self.is_malicious = False


=======
        self.seeds = [1,1,1,1,1]
        self.hits = [1,1,1,1,1]
        self.view_received = []
        self.is_malicious = False

>>>>>>> 54e1dd7e43198161fcba31ac898ab186ff7ebe35
    def remove_neighbor(self, neighbor):
        if self.neighbors:
            self.neighbors.remove(neighbor)

    def select_peer_for_communication(self):
        min_hits_index = self.hits.index(min(self.hits))
<<<<<<< HEAD
        if min_hits_index < view_size:
=======
        if min_hits_index < 5:
>>>>>>> 54e1dd7e43198161fcba31ac898ab186ff7ebe35
            selected_peer = self.neighbors[min_hits_index]
            self.hits[min_hits_index] += 1
        else : 
            selected_peer = random.choice(self.neighbors)
        return selected_peer

    def send_pull_request(self, neighbor):
        if neighbor in self.neighbors :
            neighbor.pull_list.append(self)
<<<<<<< HEAD
        else : 
            print("Error in send_pull_request")
=======
>>>>>>> 54e1dd7e43198161fcba31ac898ab186ff7ebe35

    def respond_pull_requests(self):
        for neighbor in self.pull_list:
            for selected in self.neighbors:
<<<<<<< HEAD
                if selected.ip != neighbor.ip:
                    neighbor.view_received.append(selected)
            neighbor.view_received.append(self)

    def send_push_request(self, neighbor):
        list_to_send = []
        for node in self.neighbors :
            if node.ip != neighbor.ip :
                list_to_send.append(node)
        list_to_send.append(self)        
        neighbor.view_received += list_to_send
        neighbor.push_list.append(self.ip)

    def send_push_malicious(self,neighbor,malicious_list):
        list_to_send = random.sample(malicious_list, view_size)
        neighbor.view_received += list_to_send

    def select_peers_for_communication_malicious(self, attack_force):
        list_to_contact = []
        while len(list_to_contact) <= attack_force :
            node = random.choice(self.neighbors)
            if node not in list_to_contact :
                list_to_contact.append(node)
        return list_to_contact
    
    """def respond_push_received_and_pull_requested_malicious(self):
        new_neighbor_list = []
        i = 0
        if self.view_received :
            for node in self.view_received and i < view_size:
                if node not in self.neighbors and not node.is_malicious :
                    new_neighbor_list.append(node)
                    i+=1
        self.neighbors = new_neighbor_list   """

    """def respond_push_received_and_pull_requested_malicious(self):
        new_neighbor_list = []
        i = 0
        # Ensure self.view_received is iterable and i < view_size
        for node in self.view_received:
            if i < view_size:
                if node not in self.neighbors and not node.is_malicious:
                    new_neighbor_list.append(node)
                    i += 1  # increment i only when a node is added
            else:
                break  # exit the loop once i reaches view_size
        self.neighbors = new_neighbor_list
        self.view_received.clear() """
    
    def respond_push_received_and_pull_requested_malicious(self):
        new_neighbor_list = []
        i = 0
        list_to_choose_from = set(self.view_received+self.neighbors)
        # Ensure self.view_received is iterable and i < view_size
        new_neighbor_list = random.sample(list_to_choose_from, view_size)
        self.neighbors = new_neighbor_list
        self.view_received.clear() 

    def respond_pull_requests_malicious(self,malicious_list):
        if len(malicious_list) < view_size:
            print("Not enough malicious nodes to sample from.")
            return
        list_to_send = random.sample(malicious_list, view_size)
        for node in self.pull_list :
            node.view_received += list_to_send

    def add_neighbor(self, neighbor):
        if neighbor not in self.neighbors and neighbor != self and len(self.neighbors) < view_size:
            self.neighbors.append(neighbor)

    def update_seeds(self,indice):
        list_new_neighbors = self.neighbors
        indice = indice % view_size
        indices_to_update = list(range(int(indice),int(indice+k_rho)))
        new_neighbors = []  # Préparer une nouvelle liste de voisins
        for seed_index in range(view_size):
            if seed_index in indices_to_update:
                self.seeds[seed_index] = random.getrandbits(256)
            # Trier les voisins actuels basés sur le nouveau hachage et prendre le meilleur
            sorted_neighbors = sorted(list_new_neighbors, key=lambda n: hierarchical_hash(self.seeds[seed_index], n.ip))
            best_neighbor = sorted_neighbors[0]
            new_neighbors.append(best_neighbor)
            list_new_neighbors.remove(best_neighbor)
        self.neighbors = new_neighbors 

    """def update_seeds(self):
        list_new_neighbors = self.neighbors
        new_neighbors = []  # Préparer une nouvelle liste de voisins
        for seed_index in range(view_size):  # Supposons que vous voulez maintenir 4 voisins basés sur le hachage
=======
                neighbor.view_received.append(selected)

    def send_push_request(self, neighbor):
        neighbor.view_received += self.neighbors 
        neighbor.push_list.append(self.ip)

    def add_neighbor(self, neighbor):
        if neighbor not in self.neighbors and neighbor != self and len(self.neighbors) < 5:
            self.neighbors.append(neighbor)

    def update_seeds(self):
        list_new_neighbors = self.neighbors
        new_neighbors = []  # Préparer une nouvelle liste de voisins
        for seed_index in range(5):  # Supposons que vous voulez maintenir 4 voisins basés sur le hachage
>>>>>>> 54e1dd7e43198161fcba31ac898ab186ff7ebe35
            self.seeds[seed_index] = random.getrandbits(256)
            # Trier les voisins actuels basés sur le nouveau hachage et prendre le meilleur
            sorted_neighbors = sorted(list_new_neighbors, key=lambda n: hierarchical_hash(self.seeds[seed_index], n.ip))
            best_neighbor = sorted_neighbors[0]
            new_neighbors.append(best_neighbor)
            list_new_neighbors.remove(best_neighbor)
<<<<<<< HEAD
        self.neighbors = new_neighbors  # Remplacer les anciens voisins par les nouveaux sélectionnés"""

=======
        self.neighbors = new_neighbors  # Remplacer les anciens voisins par les nouveaux sélectionnés

    """def update_seeds(self):
        if not self.neighbors:  # Si pas de voisins, pas besoin de mettre à jour
            return
        potential_new_neighbors = self.neighbors
        new_neighbors = []  # Préparer une nouvelle liste de voisins
        for seed_index in range(5):  # Supposons que vous voulez maintenir 4 voisins basés sur le hachage
            self.seeds[seed_index] = random.getrandbits(256)
            # Trier les voisins actuels basés sur le nouveau hachage et prendre le meilleur
            sorted_neighbors = sorted(self.neighbors, key=lambda n: hierarchical_hash(self.seeds[seed_index], n.ip))
            if sorted_neighbors:
                best_neighbor = sorted_neighbors[0]
                #if best_neighbor not in new_neighbors:   Éviter les doublons
                new_neighbors.append(best_neighbor)

        self.neighbors = new_neighbors  # Remplacer les anciens voisins par les nouveaux sélectionnés"""

    """def respond_push_received_and_pull_requested(self):
        # Transformer view_received en un set pour éliminer les doublons
        potential_new_neighbors = set(self.view_received)

        # Retirer les éléments qui sont déjà voisins ou le noeud lui-même
        potential_new_neighbors = {node for node in potential_new_neighbors if node not in self.neighbors and node != self}

        # Trier les potentiels nouveaux voisins basés sur un critère, par exemple, un hash (convertir en liste pour le tri)
        potential_new_neighbors = sorted(list(potential_new_neighbors), key=lambda n: hash_ip(self.seeds[0], n.ip))

        # Mettre à jour la liste des voisins avec les nouveaux candidats, en respectant la limite de 5 voisins
        updated_neighbors = self.neighbors[:]

        for new_neighbor in potential_new_neighbors:
            if len(updated_neighbors) < 5:
                updated_neighbors.append(new_neighbor)
            else:
                break  # Sortir de la boucle une fois que nous avons atteint 5 voisins

        self.neighbors = updated_neighbors
        self.view_received.clear()  # Réinitialiser la vue reçue pour la prochaine itération 
    def respond_push_received_and_pull_requested(self):
        list_for_hits = self.neighbors
            
        potential_new_neighbors = set(self.view_received + self.neighbors)
        
        new_neighbors_list = []
        for i in range(5):  # Assumant '5' comme la taille de la vue désirée
            potential_new_neighbors_sorted = sorted(
                list(potential_new_neighbors),
                key=lambda n: hash_ip(self.seeds[i], n.ip)
            )
            best_neighbor = potential_new_neighbors_sorted[0]
            new_neighbors_list.append(best_neighbor)
            
            # Mise à jour du compteur de coups
            if best_neighbor in self.neighbors:
                neighbor_index = self.neighbors.index(best_neighbor)
                self.hits[neighbor_index] += 1  # Increment hit count for the existing neighbor
            else:
                self.hits[i] = 1 # Initialiser le compteur pour un nouveau meilleur pair
            
            # Enlever le meilleur pair de l'ensemble des candidats pour la prochaine itération
            potential_new_neighbors.remove(best_neighbor)
        
        self.neighbors = new_neighbors_list
        self.view_received.clear()  # Réinitialiser la vue reçue pour la prochaine itération"""

>>>>>>> 54e1dd7e43198161fcba31ac898ab186ff7ebe35
    def respond_push_received_and_pull_requested(self):
        list_for_hits = self.neighbors
        old_hits = self.hits    
        potential_new_neighbors = set(self.view_received + self.neighbors)
        
        new_neighbors_list = []
<<<<<<< HEAD
        for i in range(view_size):  # Assumant '5' comme la taille de la vue désirée
=======
        for i in range(5):  # Assumant '5' comme la taille de la vue désirée
>>>>>>> 54e1dd7e43198161fcba31ac898ab186ff7ebe35
            potential_new_neighbors_sorted = sorted(
                list(potential_new_neighbors),
                key=lambda n: hash_ip(self.seeds[i], n.ip)
            )
            best_neighbor = potential_new_neighbors_sorted[0]
            new_neighbors_list.append(best_neighbor)
            
            # Mise à jour du compteur de coups
            if best_neighbor in self.neighbors:
                neighbor_index = self.neighbors.index(best_neighbor)
                self.hits[i] = old_hits[neighbor_index] + 1  # Increment hit count for the existing neighbor
            else:
                self.hits[i] = 1 # Initialiser le compteur pour un nouveau meilleur pair
            
            # Enlever le meilleur pair de l'ensemble des candidats pour la prochaine itération
            potential_new_neighbors.remove(best_neighbor)
        
        self.neighbors = new_neighbors_list
        self.view_received.clear()  # Réinitialiser la vue reçue pour la prochaine itération

<<<<<<< HEAD
    def create_malicious_nodes(self, nodes_list, malicious_ip_list, malicous_node_list):
        if not self.is_malicious:
            print("Node is not malicious")
            return
        
        for _ in range(100): #int(0.1*node_size)):
=======
    def create_malicious_nodes(self, nodes_list, malicious_ip_list):
        if not self.is_malicious:
            return
        
        for _ in range(10):
>>>>>>> 54e1dd7e43198161fcba31ac898ab186ff7ebe35
            # Generate a new IP with the same prefix as this node
            ip_prefix = ".".join(self.ip.split(".")[:3])
            new_ip = f"{ip_prefix}.{random.randint(0, 255)}"
            x = random.randint(50, WIDTH - 50)
            y = random.randint(50, HEIGHT - 50)
            new_node = Node(new_ip, x, y)
            new_node.is_malicious = True
            nodes_list.append(new_node)
            malicious_ip_list.append(new_node.ip)
<<<<<<< HEAD
            malicous_node_list.append(new_node)
        print(f"Created {len(malicous_node_list)} malicious nodes")

    def draw(self, screen):
        pygame.draw.circle(screen, GREEN, (self.x, self.y), 2)
        ip_surface = font.render(self.ip, True, WHITE)
        screen.blit(ip_surface, (self.x - ip_surface.get_width() // 2, self.y - ip_surface.get_height() // 2))
        for neighbor in self.neighbors:
            if neighbor.is_malicious :
                pygame.draw.line(screen, RED, (self.x, self.y), (neighbor.x, neighbor.y), 1)
            else :
                pygame.draw.line(screen, WHITE, (self.x, self.y), (neighbor.x, neighbor.y), 1)

    def draw_malicious(self, screen):
        pygame.draw.circle(screen, RED, (self.x, self.y), 2)
        ip_surface = font.render(self.ip, True, WHITE)
        screen.blit(ip_surface, (self.x - ip_surface.get_width() // 2, self.y - ip_surface.get_height() // 2))
        for neighbor in self.neighbors:
            if neighbor.is_malicious :
                pygame.draw.line(screen, BLUE, (self.x, self.y), (neighbor.x, neighbor.y), 1)
            else : 
                pygame.draw.line(screen, RED, (self.x, self.y), (neighbor.x, neighbor.y), 1)
=======

    def draw(self, screen):
        pygame.draw.circle(screen, GREEN, (self.x, self.y), 10)
        ip_surface = font.render(self.ip, True, WHITE)
        screen.blit(ip_surface, (self.x - ip_surface.get_width() // 2, self.y - ip_surface.get_height() // 2))
        for neighbor in self.neighbors:
            pygame.draw.line(screen, WHITE, (self.x, self.y), (neighbor.x, neighbor.y), 1)
>>>>>>> 54e1dd7e43198161fcba31ac898ab186ff7ebe35

nodes = []
phase = 1  # 1 for node creation, 2 for view sharing

def hash_ip(seed, ip):
    """Hash function for IP ranking."""
    hash_input = f"{seed}-{ip}"
    return hashlib.sha256(hash_input.encode()).hexdigest()

import hashlib

def hierarchical_hash(seed, ip_address):
    """
    Computes a hierarchical hash of the IP address at different subnet levels.
    
    :param seed: A random seed used for hashing.
    :param ip_address: The IP address to be hashed.
    :return: A hash value representing the hierarchical hash of the IP address.
    """
    # Convert the IP address to its integer representation
    ip_int = int(ipaddress.IPv4Address(ip_address))
    
    # Extract different parts of the IP address for hierarchical hashing
    parts = [
        (ip_int >> 24) & 0xFF,  # /8 subnet
        (ip_int >> 16) & 0xFFFF,  # /16 subnet
        (ip_int >> 8) & 0xFFFFFF,  # /24 subnet
        ip_int  # Full IP
    ]
    
    # Compute the hash for each part using the seed
    hash_parts = []
    for part in parts:
        hash_input = f"{seed}-{part}".encode()
        hash_result = hashlib.sha256(hash_input).hexdigest()
        hash_parts.append(hash_result)
    
    # Combine the individual hashes to form the final hierarchical hash
    hierarchical_hash_value = '-'.join(hash_parts)
    return hierarchical_hash_value


def generate_random_ip():
    """Generate a random IP address for simulating a unique identifier."""
    return str(ipaddress.IPv4Address(random.getrandbits(32)))

#def hash_functions():



def create_basic_node():
    #Add a new node to the network.
    ip = generate_random_ip()
    x = random.randint(50, WIDTH - 50)
    y = random.randint(50, HEIGHT - 50)
    new_node = Node(ip, x, y)
<<<<<<< HEAD
    new_node.hits = [1]*view_size
=======
    new_node.hits = [1,1,1,1,1]
>>>>>>> 54e1dd7e43198161fcba31ac898ab186ff7ebe35
    nodes.append(new_node)

def main():
    global phase
    running = True
    clock = pygame.time.Clock()
    last_share_time = 0  # Initialise le suivi du dernier partage
    counter = 0
<<<<<<< HEAD
    indice = 0
=======
>>>>>>> 54e1dd7e43198161fcba31ac898ab186ff7ebe35
    while running:
        current_time = pygame.time.get_ticks()  # Temps courant en millisecondes
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if phase == 1:
<<<<<<< HEAD
            if len(nodes) < node_size:
                create_basic_node()
                if len(nodes) == node_size:  # Transition immédiate à la phase 2
                    malicious_ips = [nodes[0].ip]# for node in nodes[:10]]
                    phase = 2
                    last_share_time = current_time  # Réinitialiser le suivi du temps pour le partage
                    """for node in nodes[0]:  # Assuming the first 10 nodes are malicious"""
                    node = nodes[0]
                    malicious_node_list = [node]
                    node.is_malicious = True
                    node.create_malicious_nodes(nodes,malicious_ips,malicious_node_list)
        elif phase == 2:
            if current_time - last_share_time > 2000:  # 5 secondes ont passé
                for node in nodes : 
                    if len(node.neighbors) < view_size :
                        node.add_neighbor(random.choice(nodes))
                    """else :
                        for i in range(1,view_size):
                            if len(node.neighbors) < view_size -2 :
                                node.add_neighbor(random.choice(malicious_node_list))
                        node.add_neighbor(random.choice(nodes))
                        node.add_neighbor(random.choice(nodes))"""
                all_have_five_neighbors = True  # On suppose d'abord que tous les nœuds ont exactement 5 voisins
                for node in nodes:
                    if len(node.neighbors) != view_size:
=======
            if len(nodes) < 100:
                create_basic_node()
                if len(nodes) == 100:  # Transition immédiate à la phase 2
                    malicious_ips = [node.ip for node in nodes[:10]]
                    phase = 2
                    last_share_time = current_time  # Réinitialiser le suivi du temps pour le partage
                    for node in nodes[:10]:  # Assuming the first 10 nodes are malicious
                        node.is_malicious = True
                        node.create_malicious_nodes(nodes,malicious_ips)
        elif phase == 2:
            if current_time - last_share_time > 2000:  # 5 secondes ont passé
                for node in nodes : 
                    for i in range(1,5):
                        if len(node.neighbors) < 5 :
                            node.add_neighbor(random.choice(nodes))
                all_have_five_neighbors = True  # On suppose d'abord que tous les nœuds ont exactement 5 voisins
                for node in nodes:
                    if len(node.neighbors) != 5:
>>>>>>> 54e1dd7e43198161fcba31ac898ab186ff7ebe35
                        all_have_five_neighbors = False
                if all_have_five_neighbors :
                    phase = 3
                    last_share_time = current_time
        elif phase == 3:
            counter += 1
<<<<<<< HEAD
            """if counter % 5 == 0:
                # Mise à jour des seeds pour chaque nœud
                for node in nodes:
                    if not node.is_malicious :
                        node.update_seeds()"""
            for node in nodes:
                    if not node.is_malicious :
                        node.update_seeds(indice)
            indice += int(counter*k_rho)
            # Logique de mise à jour des vues pour chaque nœud
            for node in nodes:
                if node.ip not in malicious_ips :
                    if node.neighbors:
                        pull_selected_node = node.select_peer_for_communication()
                        node.send_pull_request(pull_selected_node)
                        push_selected_node = node.select_peer_for_communication()
                        node.send_push_request(push_selected_node)
                        node.respond_push_received_and_pull_requested()
                        node.respond_pull_requests()
                        #node.view_received = []
                else :
                    if node.neighbors:
                        #Comportement noeud malveillant
                        pull_selected_nodes = node.select_peers_for_communication_malicious(attack_force)
                        for selected in pull_selected_nodes :
                            node.send_pull_request(selected)
                        push_selected_node = node.select_peers_for_communication_malicious(attack_force)
                        for selected in pull_selected_nodes :
                            node.send_push_request(selected)
                        node.respond_push_received_and_pull_requested_malicious()
                        node.respond_pull_requests_malicious(malicious_node_list)    
            total_views = sum(len(node.neighbors) for node in nodes[:node_size])
            malicious_views = sum(1 for node in nodes[:node_size] for view in node.neighbors if view.ip in malicious_ips)
=======
            if counter % 5 == 0:
                # Mise à jour des seeds pour chaque nœud
                for node in nodes:
                    node.update_seeds()
            # Logique de mise à jour des vues pour chaque nœud
            for node in nodes:
                if node.neighbors:
                    pull_selected_node = node.select_peer_for_communication()
                    node.send_pull_request(pull_selected_node)
                    push_selected_node = node.select_peer_for_communication()
                    node.send_push_request(push_selected_node)
                    node.respond_push_received_and_pull_requested()
                    node.respond_pull_requests()
                    #node.view_received = []
            total_views = sum(len(node.neighbors) for node in nodes)
            malicious_views = sum(1 for node in nodes for view in node.neighbors if view.ip in malicious_ips)
>>>>>>> 54e1dd7e43198161fcba31ac898ab186ff7ebe35
            if total_views > 0:
                malicious_rate = (malicious_views / total_views) * 100
                #print(f"Counter {counter}: Taux de nœuds malveillants dans les vues : {malicious_rate:.2f}%")
                if counter == 1 :
                    save_malicious_rates("rates.txt", counter, malicious_rate)
                else :
                    save_malicious_rates_append("rates.txt", counter, malicious_rate)

<<<<<<< HEAD
            if counter >= rounds:
                running = False  # Arrêter la boucle principale après 50 mises à jour

        # Dessiner le graphe
        """screen.fill(BLACK)
        for node in nodes:
            if node.is_malicious :
                node.draw_malicious(screen)
            else :
                node.draw(screen)
        pygame.display.flip()

        # Contrôler la fréquence de mise à jour
        clock.tick(10)"""

    # Nettoyage et fermeture
    #pygame.quit()
    for node in nodes:
        neighbor_ips = [neighbor.ip for neighbor in node.neighbors]
        print(f"Node {node.ip} has neighbors: {', '.join(neighbor_ips)}")
=======
            if counter >= 1000:
                running = False  # Arrêter la boucle principale après 50 mises à jour

        # Dessiner le graphe
        screen.fill(BLACK)
        for node in nodes:
            node.draw(screen)
        pygame.display.flip()

        # Contrôler la fréquence de mise à jour
        clock.tick(10)

    # Nettoyage et fermeture
    pygame.quit()
    for node in nodes:
        neighbor_ips = [neighbor.ip for neighbor in node.neighbors]
        print(f"Node {node.ip} has neighbors: {', '.join(neighbor_ips)}")
        print(f"Node {node.ip} hits are : ", node.hits)
        print(f"Node {node.ip} seeds are : ", node.seeds)
>>>>>>> 54e1dd7e43198161fcba31ac898ab186ff7ebe35

if __name__ == "__main__":
    main()
