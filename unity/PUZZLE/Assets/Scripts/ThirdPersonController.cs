using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class ThirdPersonController : MonoBehaviour
{
    public float mouseSensitivity = 0.05f;
    public Transform cameraCharacter = null;
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
    private float minXLook = -45f;
    private float maxXLook = 45f;
    private float currentXRotation;
    public Transform camAnchor;
    private float rotationSpeed = 2.0f;
    private CrosshairController crosshair;
    // Start is called before the first frame update
    void Start()
    {
        this.controller = this.GetComponent<CharacterController>();
        this.crosshair = this.GetComponent<CrosshairController>();
        Cursor.lockState = CursorLockMode.Locked;
    }

    // Update is called once per frame
    void Update()
    {
        UpdateMovement();
        UpdateViewLook();
    }
    void UpdateMovement()
    {
        float horizontalInput = Input.GetAxis("Horizontal");
        float verticalInput = Input.GetAxis("Vertical");

        if (this.controller.isGrounded == true)
        {
            downwardVelocity = 0.0f;
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
        this.controller.Move(velocity * Time.deltaTime); ;
    }
    void UpdateViewLook()
    {
        float mouseX = Input.GetAxis("Mouse X");
        float mouseY = Input.GetAxis("Mouse Y");

        smoothMouseY = Mathf.SmoothDamp(smoothMouseY, mouseY, ref currentVelocity, lookSmoothTime);
        smoothMouseX = Mathf.SmoothDamp(smoothMouseX, mouseX, ref currentVelocity, lookSmoothTime);


        //cameraCharacter.localEulerAngles = Vector3.right * cameraPitch * mouseSensitivity;
        this.transform.Rotate(Vector3.up * smoothMouseX * rotationSpeed);
        currentXRotation = currentXRotation + smoothMouseY * rotationSpeed;
        currentXRotation = Mathf.Clamp(currentXRotation, minXLook, maxXLook);

        Vector3 clampedAngle = camAnchor.eulerAngles;
        clampedAngle.x = currentXRotation;

        camAnchor.eulerAngles = clampedAngle;
        //crosshair.LookHeight(smoothMouseY * rotationSpeed);
    }
}