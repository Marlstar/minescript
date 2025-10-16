from system.lib.java import JavaClass
from lib.instance import mc

def send(packet_class: str, *args, cat: str = ""):
    # Mojang: net.minecraft.network.protocol.game.<packet_class>
    # List: https://mappings.dev/1.21.8/net/minecraft/network/protocol/game/index.html
    # Yarn: net.minecraft.network.packet.c2s.play.<packet_class>
    # List: https://maven.fabricmc.net/docs/yarn-1.21.8+build.1/net/minecraft/network/packet/c2s/play/package-summary.html
    if packet_class.startswith("class"): # Intermediary mappings
        packet_class = f"net.minecraft.{packet_class}"
    elif "c2s" in packet_class: # Yarn (fabric)
        packet_class = f"net.minecraft.network.packet.c2s.{cat or 'play'}.{packet_class}"
    else: # Mojang
        packet_class = f"net.minecraft.network.protocol.{cat or 'game'}.{packet_class}"

    pclass = JavaClass(packet_class)
    mc.player.connection.getConnection().send(pclass(*args))
