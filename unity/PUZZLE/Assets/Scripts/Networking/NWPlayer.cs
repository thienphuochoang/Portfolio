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
    [SerializeField]
    private Animator anim;
    private Vector3 moveDirection;
    private bool canDoubleJump = false;
    private bool isFlying = false;
    private Vector3 hitPoint = Vector3.zero;
    private NWSwingToDestination SwingToDestinationClass;
    private float swingSpeed = 2f;
    private float minimumSwingVectorLength = 3f;
    [SerializeField]
    private GameObject instanceAnchorObject;
    private bool doesAnchorCollide = false;
    private Transform cameraSpawnPoint;
    public GameObject cameraPrefab;
    #region Server


    #endregion

    #region Client


    public override void OnStartAuthority()
    {
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
        SwingToDestinationClass = this.GetComponent<NWSwingToDestination>();
        instanceAnchorObject = SwingToDestinationClass.instanceAnchorObj;
        anim = GetComponentInChildren<Animator>();
        cameraCharacter.transform.rotation = Quaternion.Euler(0, 0, 0);

    }

    void Update()
    {
        if (!hasAuthority)
        {
            return;
        }
        if (isFlying == false)
        {
            UpdateViewLook();
            UpdateMovement();
        }
        //UpdateSwingMovement();
        if (moveDirection == Vector3.zero)
            IdleAnimation();
        else
            RunningAnimation();

    }
    void UpdateSwingMovement()
    {
        // Swing To Destination
        float currentCameraXRotation = cameraCharacter.transform.localEulerAngles.x;

        if (currentCameraXRotation > 180f && currentCameraXRotation < 360f)
        {
            if (isFlying == true && hitPoint != Vector3.zero)
            {
                instanceAnchorObject.SetActive(true);
                upwardVelocity = 0;
                downwardVelocity = 0;
                Vector3 characterAndHitPointDir = hitPoint - this.transform.position;
                Vector3 anchorAndHitPointDir = hitPoint - instanceAnchorObject.transform.position;
                SwingToDestinationClass.MoveAnchorToHitPoint(instanceAnchorObject, hitPoint);

                // Anchor go first, hit the wall then character move
                bool checkAnchorHitFlag;
                checkAnchorHitFlag = MakeRoundPosition(anchorAndHitPointDir.magnitude, instanceAnchorObject, hitPoint);
                SwingToDestinationClass.ScaleAnchorBasedOnTime();
                if (checkAnchorHitFlag == true)
                    doesAnchorCollide = true;

                if (doesAnchorCollide == true)
                {
                    instanceAnchorObject.transform.position = hitPoint;
                    this.controller.Move(characterAndHitPointDir * Time.deltaTime * swingSpeed);
                    bool checkCharacterHitFlag;
                    checkCharacterHitFlag = MakeRoundPosition(characterAndHitPointDir.magnitude, this.transform.gameObject, hitPoint);
                    if (checkCharacterHitFlag == true)
                    {
                        SwingToDestinationClass.EndSwingAnimationAndBackToIdle();
                        Destroy(instanceAnchorObject);
                        isFlying = false;
                        doesAnchorCollide = false;
                        SwingToDestinationClass.CmdCreateAnchorInstance();
                        instanceAnchorObject = SwingToDestinationClass.instanceAnchorObj;
                    }
                }

            }
            if (Input.GetMouseButtonDown(1))
            {
                hitPoint = SwingToDestinationClass.GetHitPointFromRaycast();
                if (hitPoint != Vector3.zero)
                {
                    isFlying = true;
                    SwingToDestinationClass.SwingAnimation();
                }
            }
        }
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
    void IdleAnimation()
    {
        anim.SetFloat("Speed", 0);
    }

    void RunningAnimation()
    {
        anim.SetFloat("Speed", 1, 0.1f, Time.deltaTime);
    }

    private bool MakeRoundPosition(float vectorMagnitude, GameObject o, Vector3 hitPosition)
    {
        if (vectorMagnitude < minimumSwingVectorLength)
        {
            o.transform.position = hitPosition;
            return true;
        }
        else
            return false;
    }
    #endregion
}
