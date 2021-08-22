using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class CrosshairController : MonoBehaviour
{
    public Texture2D crosshairImage;
    private int crosshairSize = 25;
    private float crosshairMaxAngle = 95f;
    private float crosshairMinAngle = 40f;
    private float lookHeight;
    public Camera characterCamera;
    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        
    }

    public void LookHeight(float value)
    {
        lookHeight += value;
        if (lookHeight > crosshairMaxAngle || lookHeight < crosshairMinAngle)
        {
            lookHeight -= value;
        }
    }

    void OnGUI()
    {
        Vector3 screenPosition = characterCamera.WorldToScreenPoint(transform.position);
        screenPosition.y = Screen.height - screenPosition.y;
        GUI.DrawTexture(new Rect(screenPosition.x, screenPosition.y - lookHeight, crosshairSize, crosshairSize), crosshairImage);
    }
}
