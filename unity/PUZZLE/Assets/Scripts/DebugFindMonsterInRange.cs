using UnityEditor;
using UnityEngine;

[CustomEditor(typeof(FindMonstersInRange))]
public class DebugFindMonsterInRange : Editor
{
    private void OnSceneGUI()
    {
        FindMonstersInRange fov = (FindMonstersInRange)target;
        Handles.color = Color.white;
        Handles.DrawWireArc(fov.transform.position, Vector3.up, Vector3.forward, 360, fov.radius);

        Vector3 viewAngle01 = DirectionFromAngle(fov.transform.eulerAngles.y, -fov.angle / 2);
        Vector3 viewAngle02 = DirectionFromAngle(fov.transform.eulerAngles.y, fov.angle / 2);

        Handles.color = Color.yellow;
        Handles.DrawLine(fov.transform.position, fov.transform.position + viewAngle01 * fov.radius);
        //Handles.DrawLine(fov.gameObject.GetComponent<FindMonstersInRange>().eyesTransform.position, fov.gameObject.GetComponent<FindMonstersInRange>().eyesTransform.position + viewAngle01 * fov.radius);
        Handles.DrawLine(fov.transform.position, fov.transform.position + viewAngle02 * fov.radius);
        //Handles.DrawLine(fov.gameObject.GetComponent<FindMonstersInRange>().eyesTransform.position, fov.gameObject.GetComponent<FindMonstersInRange>().eyesTransform.position + viewAngle02 * fov.radius);

        if (fov.canSeePlayer)
        {
            Handles.color = Color.green;
            Handles.DrawLine(fov.transform.position, fov.playerRef.transform.position);
        }
    }

    private Vector3 DirectionFromAngle(float eulerY, float angleInDegrees)
    {
        angleInDegrees += eulerY;

        return new Vector3(Mathf.Sin(angleInDegrees * Mathf.Deg2Rad), 0, Mathf.Cos(angleInDegrees * Mathf.Deg2Rad));
    }
}