using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class ThirdPersonController : MonoBehaviour
{
    public float mouseSensitivity = 0.05f;
    public float runningSpeed = 3.0f;
    private CharacterController controller = null;
    private float lookSmoothTime = 0.02f;
    private float currentVelocity = 0.0f;
    private float smoothMouseY = 0.0f;
    private float smoothMouseX = 0.0f;
    private float gravity = 15.0f;
    private float downwardVelocity = 0.0f;
    private float upwardVelocity = 0.0f;
    private float jumpStrength = 15.0f;
    private float minXLook = -60f;
    private float maxXLook = 45f;
    private float currentXRotation;
    public Transform camAnchor;
    private float rotationSpeed = 2.0f;
    public LayerMask unseenThroughObjectsLayer;

    // This value will be controlled by GameManagerFeatures.cs
    public bool isUsingFreeLookCamera = false;



    /*this variable is a bonus height to the CameraCenter, because my character had 
	its origin at its feet, which is not where i want the center of camera rotation to be.*/
    public float yOffset;
    //The Camera (child of CameraCenter)
    public Camera cam;
    RaycastHit camHit;
    //No need to input any values for it
    private Vector3 CamDist;


    // Start is called before the first frame update
    void Start()
    {
        this.controller = this.GetComponent<CharacterController>();
        //Cursor.lockState = CursorLockMode.Locked;

        CamDist = cam.transform.localPosition;
        /* = The initial local position of the camera (relative to the CameraCenter), 
		 which is the maximal and normal Camera distance relative to it.*/
        Cursor.visible = false;
    }

    // Update is called once per frame
    void Update()
    {
        //if (Input.GetKeyDown(KeyCode.Z))
        //{
        //    Time.timeScale = 0.5f;
        //}
        if (isUsingFreeLookCamera == false)
        {
            UpdateMovement();
            UpdateViewLook();
        }
    }
    void UpdateMovement()
    {
        float horizontalInput = Input.GetAxis("Horizontal");
        float verticalInput = Input.GetAxis("Vertical");

        if (this.controller.isGrounded == true)
        {
            downwardVelocity = 0.0f;
            upwardVelocity = 0.0f;
            if (Input.GetKeyDown(KeyCode.Space))
            {
                upwardVelocity = jumpStrength;
            }
        }
        else
        {
            upwardVelocity = upwardVelocity - gravity * Time.deltaTime;
            downwardVelocity = downwardVelocity + gravity * Time.deltaTime;
        }

        Vector3 velocity = (this.transform.forward * verticalInput + this.transform.right * horizontalInput) * runningSpeed + Vector3.down * downwardVelocity + Vector3.up * upwardVelocity;
        //this.controller.Move(velocity * Time.deltaTime); ;
        this.controller.Move(velocity * Time.deltaTime);
    }
    void UpdateViewLook()
    {
        float mouseX = Input.GetAxis("Mouse X");
        float mouseY = Input.GetAxis("Mouse Y");

        smoothMouseY = Mathf.SmoothDamp(smoothMouseY, mouseY, ref currentVelocity, lookSmoothTime);
        smoothMouseX = Mathf.SmoothDamp(smoothMouseX, mouseX, ref currentVelocity, lookSmoothTime);


        this.transform.Rotate(Vector3.up * smoothMouseX * rotationSpeed);
        currentXRotation = currentXRotation + smoothMouseY * rotationSpeed;
        currentXRotation = Mathf.Clamp(currentXRotation, minXLook, maxXLook);

        Vector3 clampedAngle = camAnchor.eulerAngles;
        clampedAngle.x = currentXRotation;

        camAnchor.eulerAngles = clampedAngle;

        
        cam.transform.localPosition = CamDist;
        GameObject obj = new GameObject();
        obj.transform.SetParent(cam.transform.parent);
        obj.transform.localPosition = new Vector3(cam.transform.localPosition.x, cam.transform.localPosition.y, cam.transform.localPosition.z - 0.1f);
        //Linecast is an alternative to Raycast, using it to cast a ray between the CameraCenter 
        //  and a point directly behind the camera (to smooth things, that's why there's an "obj"
        //   GameObject, that is directly behind cam)	 
        if (Physics.Linecast(camAnchor.transform.position, obj.transform.position, out camHit, unseenThroughObjectsLayer))
        {
            //This gets executed if there's any collider in the way
            cam.transform.position = Vector3.Slerp(cam.transform.position, camHit.point, 1f);
            //cam.transform.localPosition = new Vector3(cam.transform.localPosition.x, cam.transform.localPosition.y, cam.transform.localPosition.z + 0.1f);
            cam.transform.localPosition = Vector3.Slerp(cam.transform.localPosition, new Vector3(cam.transform.localPosition.x, cam.transform.localPosition.y, cam.transform.localPosition.z + 0.1f), 1f);
        }
        //Clean up
        Destroy(obj);
        //crosshair.LookHeight(smoothMouseY * rotationSpeed);
        
    }
    private void OnCollisionEnter(Collision collision)
    {
        Debug.Log(collision.gameObject.name);
    }
}