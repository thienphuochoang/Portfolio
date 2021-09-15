using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.Events;
public class SetObjectAsButton : MonoBehaviour
{
    public UnityEvent clickButtonEvent = new UnityEvent();
    private GameObject button;
    // Start is called before the first frame update
    void Start()
    {
        button = this.gameObject;
    }

    // Update is called once per frame
    void Update()
    {
        if (Input.GetMouseButtonUp(0))
        {
            Ray ray = Camera.main.ScreenPointToRay(Input.mousePosition);
            RaycastHit hit;
            if (Physics.Raycast(ray, out hit) && hit.collider.gameObject == this.gameObject)
            {
                clickButtonEvent.Invoke();
            }
        }
    }
}
