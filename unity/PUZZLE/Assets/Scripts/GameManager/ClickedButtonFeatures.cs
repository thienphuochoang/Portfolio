using UnityEngine;
using UnityEngine.EventSystems;
using UnityEngine.Events;
using Sirenix.OdinInspector;
public class ClickedButtonFeatures : MonoBehaviour, IPointerDownHandler, IPointerEnterHandler
{

    public enum ButtonFeatures { NULL, SKILL_SELECTION, BACK, OK }
    public ButtonFeatures buttonFeatureAssigned = ButtonFeatures.NULL;
    [EnableIf("buttonFeatureAssigned", ButtonFeatures.SKILL_SELECTION)]
    public UnityEvent leftClick;
    [EnableIf("buttonFeatureAssigned", ButtonFeatures.SKILL_SELECTION)]
    public UnityEvent hover;
    [EnableIf("buttonFeatureAssigned", ButtonFeatures.BACK)]
    public UnityEvent backButtonOnClick;
    [EnableIf("buttonFeatureAssigned", ButtonFeatures.OK)]
    public UnityEvent loadLevelButtonOnClick;
    // Start is called before the first frame update
    void Start()
    {
    }

    // Update is called once per frame
    void Update()
    {
    }
    public void OnPointerDown(PointerEventData eventData)
    {
        GameObject clickedButton = eventData.pointerCurrentRaycast.gameObject;
        switch (buttonFeatureAssigned)
        {
            // Default case
            default:
                {
                    Debug.Log("NULL state");
                }
                break;
            case ButtonFeatures.SKILL_SELECTION:
                {
                    if (eventData.button == PointerEventData.InputButton.Left)
                    {
                        leftClick.Invoke();
                    }
                }
                break;

            case ButtonFeatures.BACK:
                {
                    backButtonOnClick.Invoke();
                }
                break;
            case ButtonFeatures.OK:
                {
                    loadLevelButtonOnClick.Invoke();
                }
                break;
        }
    }
    public void OnPointerEnter(PointerEventData eventData)
    {
        switch (buttonFeatureAssigned)
        {
            case ButtonFeatures.SKILL_SELECTION:
                {
                    hover.Invoke();
                }
                break;
        }
    }
}