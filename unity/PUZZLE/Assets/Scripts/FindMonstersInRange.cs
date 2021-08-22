using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class FindMonstersInRange : MonoBehaviour
{
    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        GetMonstersListInRange(this.transform.position, 1f);
    }
    private void OnDrawGizmos()
    {
        Gizmos.color = Color.red;
        //Use the same vars you use to draw your Overlap SPhere to draw your Wire Sphere.
        Gizmos.DrawWireSphere(this.transform.position, 1f);
    }
    public List<GameObject> GetMonstersListInRange(Vector3 center, float radius)
    {
        List<GameObject> monsterList = new List<GameObject>();
        Collider[] hitColliders = Physics.OverlapSphere(center, radius);
        foreach (var hitCollider in hitColliders)
        {
            if (hitCollider.gameObject.tag.Contains("Monster"))
            {
                monsterList.Insert(0, hitCollider.gameObject);
                Debug.Log(hitCollider.gameObject.name);
            }
        }
        return monsterList;
    }
}
