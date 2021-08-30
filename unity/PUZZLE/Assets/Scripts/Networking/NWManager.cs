using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using Mirror;
public class NWManager : NetworkManager
{
    /*
    public override void OnClientConnect(NetworkConnection conn)
    {
        base.OnClientConnect(conn);
        //Debug.Log("I connected to the server!");
    }
    */

    public override void OnServerAddPlayer(NetworkConnection conn)
    {
        base.OnServerAddPlayer(conn);
        NWPlayer player = conn.identity.GetComponent<NWPlayer>();
        //Debug.Log($"There are now {numPlayers} players");
    }
}
