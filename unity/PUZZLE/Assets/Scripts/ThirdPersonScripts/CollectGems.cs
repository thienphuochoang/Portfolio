using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class CollectGems : MonoBehaviour
{
    private GeneralParticleFeatures generalParticleFeatures;
    private float duration = 5f;
    private float speed = 2f;
    public GameObject justCollectedGem;
    // Start is called before the first frame update
    void Start()
    {
        generalParticleFeatures = FindObjectOfType<GeneralParticleFeatures>();
    }

    // Update is called once per frame
    void Update()
    {
    }
    private void OnTriggerEnter(Collider other)
    {
        if (other.gameObject.layer == LayerMask.NameToLayer("Gems"))
        {
            float i = 0f;
            float rate = (1 / duration) * speed;
            Vector3 currentScale = other.transform.localScale;
            while (i < 1f)
            {
                i += Time.deltaTime * rate;
                other.transform.localScale = Vector3.Lerp(currentScale, new Vector3(0, 0, 0), i);
            }
            justCollectedGem = other.gameObject;
            generalParticleFeatures.AddCollectedGemEffect(other.transform.position, Camera.current.transform.rotation);
            other.gameObject.SetActive(false);
            //Destroy(other.gameObject);
            GetComponent<PlayerAttributes>().attributes._collectedGems += 1;
        }
    }
}
