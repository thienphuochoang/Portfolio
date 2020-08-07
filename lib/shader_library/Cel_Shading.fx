cbuffer UpdatePerFrame : register(b0)
{
    matrix World : World;
    matrix View : View;
    matrix Projection : Projection;
    matrix WorldViewProjection : WorldViewProjection;
    matrix WorldInverseTranspose : WorldInverseTranspose;
    matrix ViewInverse : ViewInverse;

    float4 Color
    <
        string Object = "Object Settings";
        string UIWidget = "Color";
        string UIName = "Object Color";
    > = {1.0f, 1.0f, 1.0f, 1.0f};

    float Glossiness
    <
        string Object = "Object Settings";
        string UIName = "Object Glossiness";
        float UIMin = 0.0f;
        float UIMax = 100.0f;
        float UIStep = 1.0f;
    > = 32.0f;

    float4 AmbientColor
    <
        string Object = "Object Settings";
        string UIWidget = "Color";
        string UIName = "Object Ambient Color";
    > = {0.4f, 0.4f, 0.4f, 1.0f};

    float4 SpecularColor
    <
        string Object = "Object Settings";
        string UIWidget = "Color";
        string UIName = "Object Specular Color";
    > = {0.9f, 0.9f, 0.9f, 1.0f};

    float RimThreshold
    <
        string Object = "Rim Settings";
        string UIName = "Rim Threshold";
        float UIMin = 0.0f;
        float UIMax = 1.0f;
        float UIStep = 0.1f;
    > = 0.1f;

    float RimAmount
    <
        string Object = "Rim Settings";
        string UIName = "Rim Amount";
        float UIMin = 0.0f;
        float UIMax = 1.0f;
        float UIStep = 0.1f;
    > = 0.716f;

    float4 RimColor
    <
        string Object = "Rim Settings";
        string UIWidget = "Color";
        string UIName = "Rim Color";
    > = {1.0f, 1.0f, 1.0f, 1.0f};

    float3 light0Dir : DIRECTION 
    < 
        string Object = "Light 0";
        string UIName = "Light 0 Direction"; 
        string Space = "World";
    > = {1.0f, 1.0f, 1.0f};
    float4 light0Color
    < 
        string Object = "Light 0";
        string UIWidget = "Color";
        string UIName = "Light Color";
    > = {1.0f, 1.0f, 1.0f, 1.0f};

    float light0Intensity
    <
        string Object = "Light 0";
        float UIMin = 0.0f;
        float UIMax = 1.0f;
        float UIStep = 0.1f;
        string UIWidget = "slider";
    > = 1.0f;
}
// float3 LineColor
// <
//     string Object = "Line Settings";
//     string UIWidget = "Color";
//     string UIName = "Line Color";
// > = {0.0f, 0.0f, 0.0f};

// float LineThickness
// <
//     string Object = "Line Settings";
//     float UIMin = 0.0f;
//     float UIMax = 10.0f;
//     float UIStep = 0.01f;
//     string UIName = "Line Thickness";
// > = 0.03f;

texture Texture;
SamplerState textureSampler
{
    Texture = (Texture);
    MinFilter = Linear;
    MagFilter = Linear;
    AddressU = Clamp;
    AddressV = Clamp;
};

struct VERTEX_INPUT 
{
    float3 Position     : POSITION;
    float2 Texcoord     : TEXCOORD0;
    float3 Normal       : NORMAL;
};

struct PIXEL_INPUT 
{
    float4 Position         : SV_POSITION;
    float2 Texcoord         : TEXCOORD0;
    float3 WorldNormal      : NORMAL;
    float3 WorldPosition    : POSITIONT;
};

PIXEL_INPUT std_VS(VERTEX_INPUT input)
{
    PIXEL_INPUT output;
    output.Position = mul(float4(input.Position, 1.0f), WorldViewProjection);
    output.WorldNormal = normalize(mul(float4(input.Normal, 1.0f), WorldInverseTranspose));
    output.WorldPosition = mul(float4(input.Position, 1.0f), World);
    output.Texcoord = input.Texcoord;
    
    return output;
}

float4 std_PS(PIXEL_INPUT input) : SV_Target
{

    
    float3 viewDir  = normalize(input.WorldPosition - ViewInverse[3].xyz);
    float3 OppositeViewDir = -viewDir;
    
    float NdotL = dot(input.WorldNormal, viewDir);
    float intensity = dot(normalize(-light0Dir), input.WorldNormal);
    if(intensity < 0)
        intensity = 0;
    // float3 R = reflect(-viewDir, input.WorldNormal);
    //if(NdotL < 0)
        //NdotL = 0;
 
    // Calculate what would normally be the final color, including texturing and diffuse lighting
    //float4 light = light0Color * light0Intensity;
    float4 texColor = tex2D(textureSampler, input.Texcoord);
    texColor.a = 1.0;
 
    // Discretize the intensity, based on a few cutoff points


    float4 light = light0Intensity * light0Color;

    float3 halfVector = normalize(-light0Dir + OppositeViewDir);
    float NdotH = dot(input.WorldNormal, halfVector);
    float specularIntensity = pow(NdotH * light0Intensity, Glossiness * Glossiness);
    //float specularIntensitySmooth = smoothstep(0.005, 0.01, specularIntensity);
    float4 specular = specularIntensity * SpecularColor;
    float4 diffuse = NdotH;
    diffuse = round(intensity * 5) / 5 * diffuse;
    specular = round(intensity * 5) / 5 * specular;

    float rimDot = 1 - dot(OppositeViewDir, input.WorldNormal);
    float rimIntensity = rimDot * pow(NdotL, RimThreshold);
    rimIntensity = smoothstep(RimAmount - 0.01, RimAmount + 0.01, rimIntensity);
    float4 rim = rimIntensity * RimColor;

    float4 finalColor = saturate((specular + diffuse) * Color)  + light + AmbientColor + rim;
    return finalColor;
}
///// TECHNIQUES ///////////////////////////// 
technique11 CartoonCelShading 
{
    pass p0 
    {
        SetVertexShader(CompileShader(vs_5_0,std_VS()));
        SetGeometryShader(NULL);
        //SetGeometryShader(CompileShader(gs_5_0,std_GS()));
        SetPixelShader(CompileShader(ps_5_0,std_PS()));
    }
}
/////////////////////////////////////// eof //