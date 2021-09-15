using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class SwapCameraFeatures : MonoBehaviour
{
    [Header("Player Settings")]
    public GameObject thirdPersonController;
    private Transform currentCharacterCameraAnchor;
    private Camera cam;
    private string cameraTag = "PlayerCamera";

    [Header("Free Look Camera Settings")]
    public GameObject freeLookCameraPrefab;
    private GameObject instanceFreeLookCamera = null;
    private Vector3 lastKnownFreeLookCameraPosition = Vector3.zero;
    // Start is called before the first frame update
    void Start()
    {
        currentCharacterCameraAnchor = thirdPersonController.GetComponent<ThirdPersonController>().camAnchor;

        Transform cameraTransform;
        cameraTransform = thirdPersonController.GetComponent<TransformIntoAnotherObj>().RecursiveFindChild(thirdPersonController.transform, cameraTag, "tag");
        cam = cameraTransform.gameObject.GetComponent<Camera>();
    }

    // Update is called once per frame
    void Update()
    {
        EnableFreeLookCamera();
    }

    void EnableFreeLookCamera()
    {
        if (Input.GetKeyDown(KeyCode.Tab))
        {
            if (instanceFreeLookCamera == null)
            {
                if (lastKnownFreeLookCameraPosition == Vector3.zero)
                {
                    currentCharacterCameraAnchor.gameObject.SetActive(false);
                    instanceFreeLookCamera = Instantiate(freeLookCameraPrefab, cam.transform.position, cam.transform.rotation);
                    instanceFreeLookCamera.SetActive(true);
                    lastKnownFreeLookCameraPosition = instanceFreeLookCamera.transform.position;
                    thirdPersonController.GetComponent<ThirdPersonController>().isUsingFreeLookCamera = true;
                }
            }
            else
            {
                if (instanceFreeLookCamera.activeSelf == true)
                {
                    currentCharacterCameraAnchor.gameObject.SetActive(true);
                    instanceFreeLookCamera.SetActive(false);
                    thirdPersonController.GetComponent<ThirdPersonController>().isUsingFreeLookCamera = false;
                    lastKnownFreeLookCameraPosition = instanceFreeLookCamera.transform.position;
                }
                else
                {
                    instanceFreeLookCamera.SetActive(true);
                    currentCharacterCameraAnchor.gameObject.SetActive(false);
                    thirdPersonController.GetComponent<ThirdPersonController>().isUsingFreeLookCamera = true;
                    instanceFreeLookCamera.transform.position = Vector3.Slerp(instanceFreeLookCamera.transform.position, lastKnownFreeLookCameraPosition, 1f);
                    instanceFreeLookCamera.transform.rotation = cam.transform.rotation;
                }
            }
        }
    }
}
