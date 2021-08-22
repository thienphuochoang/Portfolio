using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using Mirror;
public class NWPlayer : NetworkBehaviour
{
    public float mouseSensitivity = 2f;
    private float cameraPitch = 0.0f;
    [SerializeField]
    private Transform cameraCharacter = null;
    [SyncVar]
    public float runningSpeed = 3.0f;
    [SerializeField]
    private CharacterController controller = null;
    private float lookSmoothTime = 0.02f;
    private float currentVelocity = 0.0f;
    private float smoothMouseY = 0.0f;
    private float smoothMouseX = 0.0f;
    private float gravity = 15.0f;
    private float downwardVelocity = 0.0f;
    private float upwardVelocity = 0.0f;
    private float jumpStrength = 12f;
    private Animator anim;
    private Vector3 moveDirection;
    private bool canDoubleJump = false;
    private bool isFlying = false;
    private Vector3 hitPoint = Vector3.zero;
    private SwingToDestination SwingToDestinationClass;
    private float swingSpeed = 2f;
    private float minimumSwingVectorLength = 3f;
    private GameObject instanceAnchorObject;
    private bool doesAnchorCollide = false;
    private Transform cameraSpawnPoint;
    public GameObject cameraPrefab;
    #region Server


    #endregion

    #region Client


    public override void OnStartClient()
    {
        //SwingToDestinationClass = this.GetComponent<SwingToDestination>();
        //instanceAnchorObject = SwingToDestinationClass.instanceAnchorObj;
        /*
        for (int i = 0; i < this.transform.childCount; i++)
        {
            if (this.transform.GetChild(i).name == "CameraSpawnPoint")
            {
                cameraSpawnPoint = this.transform.GetChild(i);
            }
        }
        if (isLocalPlayer)
        {
            GameObject tempCam;
            tempCam = Instantiate(cameraPrefab, cameraSpawnPoint.position, Quaternion.Euler(0f, 0f, 0f), this.transform);
            cameraCharacter = tempCam.transform;
            cameraCharacter.parent = cameraSpawnPoint.transform;
            cameraCharacter.position = cameraSpawnPoint.transform.position;
            cameraCharacter.rotation = cameraSpawnPoint.transform.rotation;
        }
        */


        this.controller = this.GetComponent<CharacterController>();
 
        for (int i = 0; i < this.transform.childCount; i++)
        {
            if (this.transform.GetChild(i).name.Contains("CharacterCamera"))
            {
                cameraCharacter = this.transform.GetChild(i);
                if (!isLocalPlayer)
                    cameraCharacter.gameObject.SetActive(false);
            }
        }

        //Cursor.lockState = CursorLockMode.Locked;
        //anim = GetComponentInChildren<Animator>();
        cameraCharacter.transform.rotation = Quaternion.Euler(0, 0, 0);

    }

    void Update()
    {
        UpdateViewLook();
        UpdateMovement();
    }

    private void UpdateMovement()
    {

        float horizontalInput = Input.GetAxis("Horizontal");
        float verticalInput = Input.GetAxis("Vertical");
        moveDirection = new Vector3(0, 0, verticalInput);
        //anim.speed = 1;

        // Jump
        if (Input.GetKeyDown(KeyCode.Space))
        {
            if (this.controller.isGrounded == true)
            {
                canDoubleJump = true;
                downwardVelocity = 0f;
                upwardVelocity = jumpStrength;
            }
            else
            {
                if (canDoubleJump == true)
                {
                    if (Input.GetKeyDown(KeyCode.Space))
                    {
                        upwardVelocity = upwardVelocity + jumpStrength;
                        canDoubleJump = false;
                    }
                }
            }
        }

        upwardVelocity = upwardVelocity - gravity * Time.deltaTime;
        downwardVelocity = downwardVelocity + gravity * Time.deltaTime;

        Vector3 velocity = (this.transform.forward * verticalInput + this.transform.right * horizontalInput) * runningSpeed + Vector3.down * downwardVelocity + Vector3.up * upwardVelocity;
        this.controller.Move(velocity * Time.deltaTime);
    }

    void UpdateViewLook()
    {

        float mouseX = Input.GetAxis("Mouse X");
        float mouseY = Input.GetAxis("Mouse Y");

        smoothMouseY = Mathf.SmoothDamp(smoothMouseY, mouseY, ref currentVelocity, lookSmoothTime);
        smoothMouseX = Mathf.SmoothDamp(smoothMouseX, mouseX, ref currentVelocity, lookSmoothTime);

        cameraPitch -= smoothMouseY;
        cameraPitch = Mathf.Clamp(cameraPitch, -30f, 30f);

        cameraCharacter.localEulerAngles = Vector3.right * cameraPitch * mouseSensitivity;
        this.transform.Rotate(Vector3.up * smoothMouseX * mouseSensitivity);
    }
    #endregion
}
