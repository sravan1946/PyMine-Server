# A flexible and fast Minecraft server software written completely in Python.
# Copyright (C) 2021 PyMine

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

from pymine.net.packets.play.player import PlayDisconnect
from pymine.types.stream import Stream
from pymine.types.packet import Packet
from pymine.server import server


@server.api.register.on_packet("play", 0x00)
async def on_teleport_confirm(stream: Stream, packet: Packet) -> None:
    player = await server.playerio.fetch_player(server.cache.uuid[stream.remote])

    if player.teleport_id != packet.teleport_id:
        # await server.send_packet(
        #     stream, PlayDisconnect(f"Invalid teleport ID ({repr(player.teleport_id)} != {repr(packet.teleport_id)}).")
        # )

        server.console.debug(
            f"Warning, invalid teleport ID. ({repr(player.teleport_id)} != {repr(packet.teleport_id)})"
        )
