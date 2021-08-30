using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.AI;

public class MoveToPoint : IState
{
    public List<Transform> _pointList = new List<Transform>();
    private int destPoint = 0;
    private Animator _anim;
    private NPC _npc;
    private Vector3 lastPosition;

    public MoveToPoint(List<Transform> pointList, Animator anim, NPC npc)
    {
        _pointList = pointList;
        _anim = anim;
        _npc = npc;
    }
    public void Tick()
    {
        if (!_npc.GetComponent<NavMeshAgent>().pathPending && _npc.GetComponent<NavMeshAgent>().remainingDistance < 0.5f)
            GotoNextPoint();
    }
    void GotoNextPoint()
    {
        // Returns if no points have been set up
        if (_pointList.Count == 0)
            return;
        WalkingAnimation();

        // Set the agent to go to the currently selected destination.
        _npc.GetComponent<NavMeshAgent>().destination = _pointList[destPoint].position;

        // Calculate the orientation based on the velocity of the agent
        Vector3 orientation = _npc.GetComponent<NavMeshAgent>().transform.position - lastPosition;
        // Check if the agent has some minimal velocity
        if (orientation.sqrMagnitude > 0.1f)
        {
            // We don't want him to look up or down
            orientation.y = 0;
            // Use Quaternion.LookRotation() to set the model's new rotation and smooth the transition with Quaternion.Lerp();
            _npc.GetComponent<NavMeshAgent>().transform.rotation = Quaternion.Lerp(_npc.GetComponent<NavMeshAgent>().transform.rotation, Quaternion.LookRotation(_npc.GetComponent<NavMeshAgent>().transform.position - lastPosition), Time.deltaTime * 8);
        }
        else
        {
            // If the agent is stationary we tell him to assume the proxy's rotation
            _npc.GetComponent<NavMeshAgent>().transform.rotation = Quaternion.Lerp(_npc.GetComponent<NavMeshAgent>().transform.rotation, Quaternion.LookRotation(_npc.GetComponent<NavMeshAgent>().transform.forward), Time.deltaTime * 8);
        }
        // This is needed to calculate the orientation in the next frame
        lastPosition = _npc.GetComponent<NavMeshAgent>().transform.position;

        // Choose the next point in the array as the destination,
        // cycling to the start if necessary.
        if (Vector3.Distance(_pointList[destPoint].position, _npc.transform.position) < 0.5f)
            destPoint = (destPoint + 1) % _pointList.Count;
    }

    public void OnEnter()
    {
        _npc.GetComponent<NavMeshAgent>().enabled = true;
        _npc.GetComponent<NavMeshObstacle>().enabled = false;
    }
    public void OnExit() { }

    void WalkingAnimation()
    {
        _anim.SetFloat("Speed", 1);
    }
}
/*
using UnityEngine;
using System.Collections;
public class enemyMovement : MonoBehaviour
{
    public Transform player;
    public Transform model;
    public Transform proxy;
    NavMeshAgent agent;
    NavMeshObstacle obstacle;
    Vector3 lastPosition;
    void Start() 
    { 
        agent = proxy.GetComponent<NavMeshAgent>(); 
        obstacle = proxy.GetComponent<NavMeshObstacle>(); 
    }
    void Update()
    {
        // Test if the distance between the agent (which is now the proxy) and the player
        // is less than the attack range (or the stoppingDistance parameter)
        if ((player.position - proxy.position).sqrMagnitude < Mathf.Pow(agent.stoppingDistance, 2))
        { 
            // If the agent is in attack range, become an obstacle and 
            // disable the NavMeshAgent component
            obstacle.enabled = true; 
            agent.enabled = false; 
        } 
        else 
        {
            // If we are not in range, become an agent again
            obstacle.enabled = false;
            agent.enabled = true;
            // And move to the player's position
            agent.destination = player.position; 
        } 
        model.position = Vector3.Lerp(model.position, proxy.position, Time.deltaTime * 2); 
        // Calculate the orientation based on the velocity of the agent
        Vector3 orientation = model.position - lastPosition; 
        // Check if the agent has some minimal velocity
        if (orientation.sqrMagnitude > 0.1f)
        { 
            // We don't want him to look up or down
            orientation.y = 0;
            // Use Quaternion.LookRotation() to set the model's new rotation and smooth the transition with Quaternion.Lerp();
            model.rotation = Quaternion.Lerp(model.rotation, Quaternion.LookRotation(model.position - lastPosition), Time.deltaTime * 8);
        } 
        else
        { 
            // If the agent is stationary we tell him to assume the proxy's rotation
            model.rotation = Quaternion.Lerp(model.rotation, Quaternion.LookRotation(proxy.forward), Time.deltaTime * 8); 
        }
        // This is needed to calculate the orientation in the next frame
        lastPosition = model.position;
    }
}
*/
