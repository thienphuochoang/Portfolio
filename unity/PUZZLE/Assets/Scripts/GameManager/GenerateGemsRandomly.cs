using System.Collections;
using System.Collections.Generic;
using System;
using System.Linq;
using UnityEngine;

public class GenerateGemsRandomly : MonoBehaviour
{
    public GameObject spawningArea;
    public int maximumSpawningGems = 5;
    public List<GameObject> gemList = new List<GameObject>();
    public List<Sprite> gemImageList = new List<Sprite>();
    private Dictionary<GameObject, Sprite> instantiateGemDictionary = new Dictionary<GameObject, Sprite>();
    public Dictionary<GameObject, Sprite> chosenGemDictionary = new Dictionary<GameObject, Sprite>();
    private GameObject gemParentObject;

    private float maxDistance = 200f;
    void Awake()
    {
        instantiateGemDictionary = CreateGemDictionary();
        instantiateGemDictionary = Shuffle(instantiateGemDictionary);
        //SpawnGems();
    }
    // Start is called before the first frame update
    void Start()
    {
        gemParentObject = new GameObject();
        gemParentObject.name = "Gems";
        SpawnGems(instantiateGemDictionary);
    }
    // Update is called once per frame
    void Update()
    {
        
    }
    private Vector3 GetHighSpawningPoint()
    {
        float x = UnityEngine.Random.Range(spawningArea.GetComponent<BoxCollider>().bounds.min.x, spawningArea.GetComponent<BoxCollider>().bounds.max.x);
        float y = spawningArea.GetComponent<BoxCollider>().bounds.max.y;
        float z = UnityEngine.Random.Range(spawningArea.GetComponent<BoxCollider>().bounds.min.z, spawningArea.GetComponent<BoxCollider>().bounds.max.z);
        Vector3 result = new Vector3(x, y, z);
        return result;
    }
    private void SpawnGems(Dictionary<GameObject, Sprite> instantiateGemDictionary)
    {
        RaycastHit hit;
        int i = 0;
        foreach (KeyValuePair<GameObject, Sprite> instantiateGemPair in instantiateGemDictionary)
        {
            if (i < maximumSpawningGems)
            {
                Vector3 position = GetHighSpawningPoint();
                if (Physics.Raycast(position, Vector3.down, out hit, maxDistance))
                {
                    GameObject spawnGem = Instantiate(instantiateGemPair.Key, hit.point + new Vector3(0, 2f, 0), Quaternion.Euler(-90, 0, 0), gemParentObject.transform);
                    chosenGemDictionary.Add(spawnGem, instantiateGemPair.Value);
                    i += 1;
                }

            }
        }
    }
    private Dictionary<GameObject, Sprite> CreateGemDictionary()
    {
        Dictionary<GameObject, Sprite> instantiateGemDictionary = new Dictionary<GameObject, Sprite>();
        for (int i = 0; i < gemList.Count; i++)
        {
            instantiateGemDictionary.Add(gemList[i], gemImageList[i]);
        }
        return instantiateGemDictionary;
    }
    private Dictionary<TKey, TValue> Shuffle<TKey, TValue>(Dictionary<TKey, TValue> source)
    {
        System.Random r = new System.Random();
        return source.OrderBy(x => r.Next()).ToDictionary(item => item.Key, item => item.Value);
    }
}
