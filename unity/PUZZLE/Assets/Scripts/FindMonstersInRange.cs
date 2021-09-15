using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class FindMonstersInRange : MonoBehaviour
{
    public float radius;
    [Range(0,360)]
    public float angle;

    public GameObject playerRef;

    public LayerMask targetMask;
    public LayerMask obstructionMask;

    public bool canSeePlayer = false;
    public float timer = 0f;
    private float accelerationIncreasementPerSecond = 2f;
    public GameObject alertIcon;
    public Sprite yellowAlertSprite;
    public Sprite redAlertSprite;
    public bool redAlertPlayerTrigger = false;
    public Vector3 lastKnownLocation;
    private float redAlertMaximumTime = 5f;

    // Start is called before the first frame update
    void Start()
    {
        playerRef = GameObject.FindGameObjectWithTag("Player");
        //StartCoroutine(FOVRoutine());
    }

    // Update is called once per frame
    void Update()
    {
        playerRef = GameObject.FindGameObjectWithTag("Player");
        canSeePlayer = CheckFieldOfView();
        if (canSeePlayer == false)
        {
            timer -= accelerationIncreasementPerSecond * Time.deltaTime;
            if (timer < 0)
            {
                timer = 0;
            }
        }
        else
        {
            float accelerationBasedOnDistance = CalculateAccelerationBasedOnDistance();
            lastKnownLocation = playerRef.transform.position;
            timer += accelerationBasedOnDistance * Time.deltaTime;
        }
        AssignTriggerBasedOnTime(timer);
    }
    private float CalculateAccelerationBasedOnDistance()
    {
        float playerAndNPCDistance = Vector3.Distance(transform.position, playerRef.transform.position);
        return (radius - playerAndNPCDistance);
    }
    private bool CheckFieldOfView()
    {
        Collider[] rangeChecks = Physics.OverlapSphere(transform.position, radius, targetMask);

        if (rangeChecks.Length != 0)
        {
            Transform target = rangeChecks[0].transform;
            Vector3 directionToTarget = (target.position - transform.position).normalized;

            if (Vector3.Angle(transform.forward, directionToTarget) < angle / 2)
            {
                float distanceToTarget = Vector3.Distance(transform.position, target.position);

                if (!Physics.Raycast(transform.position, directionToTarget, distanceToTarget, obstructionMask))
                {
                    return true;
                }
            }
        }
        return false;
    }
    private void AssignTriggerBasedOnTime(float cooldownTime)
    {
        if (cooldownTime <= 0)
        {
            ResetToDefault();
        }
        else if (cooldownTime > 0 && cooldownTime < redAlertMaximumTime)
        {
            float alertIconScale = cooldownTime / redAlertMaximumTime;
            SwitchToYellowAlert(alertIconScale);
        }
        else if (cooldownTime > redAlertMaximumTime)
        {
            cooldownTime = redAlertMaximumTime;
            float alertIconScale = cooldownTime / redAlertMaximumTime;
            SwitchToRedAlert(alertIconScale);
        }
    }
    private void SwitchToRedAlert(float iconScale)
    {
        alertIcon.SetActive(true);
        alertIcon.GetComponent<SpriteRenderer>().sprite = redAlertSprite;
        alertIcon.transform.localScale = new Vector3(iconScale, iconScale, iconScale);
        //lastKnownLocation = playerRef.transform.position;
        //GameObject cube = GameObject.CreatePrimitive(PrimitiveType.Cube);
        //cube.transform.position = lastKnownLocation;
        redAlertPlayerTrigger = true;
    }
    private void SwitchToYellowAlert(float iconScale)
    {
        alertIcon.SetActive(true);
        alertIcon.GetComponent<SpriteRenderer>().sprite = yellowAlertSprite;
        alertIcon.transform.localScale = new Vector3(iconScale, iconScale, iconScale);
        redAlertPlayerTrigger = false;
        //cooldownRedAlertTime = 0;
    }
    private void ResetToDefault()
    {
        alertIcon.transform.localScale = new Vector3(0, 0, 0);
        alertIcon.SetActive(false);
        redAlertPlayerTrigger = false;
        //cooldownRedAlertTime = 0;
    }
}
