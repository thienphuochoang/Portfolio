float4x4 WorldViewProjection : WorldViewProjection < string UIWidget="None"; >;
float4x4 World : World < string UIWidget="None"; >;
float4x4 View : View < string UIWidget="None"; >;
float4x4 Projection : Projection < string UIWidget="None"; >;


int Map_Resolution_Size_Width
<
    string UIName = "Map Resolution Width";
    int UIMin = 256;
    int UIMax = 4096;
    int UIStep = 1;
    string UIWidget = "slider";
> = 512;
int Map_Resolution_Size_Height
<
    string UIName = "Map Resolution Height";
    int UIMin = 256;
    int UIMax = 4096;
    int UIStep = 1;
    string UIWidget = "slider";
> = 512;
int Texel_Density
<
    string UIName = "Texel Density";
    int UIMin = 0;
    int UIMax = 4096;
    int UIStep = 1;
    string UIWidget = "slider";
> = 0;

struct VERTEX_INPUT 
{
    float3 Position     : POSITION;
    float2 Texcoord     : TEXCOORD0;
};

struct GEOMETRY_INPUT
{
    float4 Position : SV_POSITION;
    float3 Texcoord : TEXCOORD0;
    
};

struct PIXEL_INPUT 
{
    float4 Position    : SV_POSITION;
    float3 Texcoord    : TEXCOORD0;
};



GEOMETRY_INPUT std_VS(VERTEX_INPUT input)
{
    GEOMETRY_INPUT output = (GEOMETRY_INPUT)0;
    output.Position = mul( float4(input.Position,1), WorldViewProjection );
    output.Texcoord = float3(input.Texcoord, 0.0);
    return output;
}

float findTriangleArea(float3 A, float3 B, float3 C)
{
    float3 vectorAB = B - A;
    float3 vectorAC = C - A;
    float3 vectorBC = C - B;
    float lengthAB = length(vectorAB);
    float lengthAC = length(vectorAC);
    float lengthBC = length(vectorBC);
    // Using Heron's formula to calculate area of triangle 
    float s = (lengthAB + lengthAC + lengthBC) / 2;
    float areaOfTriangle = sqrt(s * ((s - lengthAB) * (s - lengthAC) * (s - lengthBC)));
    return areaOfTriangle;
}

float ConvertMinMaxTo01(float MinValue, float MaxValue, float Value)
{
    return (Value - MinValue) / (MaxValue - MinValue);
}

float3 TriLerp(float3 Color1, float3 Color2, float3 Color3, float MixValue, float MinValue, float MaxValue1, float MaxValue2)
{
    float lerpValue1 = ConvertMinMaxTo01(MinValue, MaxValue1, MixValue);
    float lerpValue2 = ConvertMinMaxTo01(MaxValue1, MaxValue2, MixValue);

    float3 finalColor = lerp(Color1, Color2, lerpValue1);
    finalColor = lerp(finalColor, Color3, lerpValue2);
    return finalColor;
}

float3 GetColorOfTriangle(float currentDensity)
{

    float value = clamp(currentDensity / Texel_Density, 0.5, 2.0);

    float3 correctColor = float3(0.0, 1.0, 0.0);
    float3 minColor = float3(1.0, 0.0, 0.0);
    float3 maxColor = float3(0.0, 0.0, 1.0);

    return TriLerp(minColor, correctColor, maxColor, value, 0.5, 1.0, 2.0);
}



[maxvertexcount(3)]
void std_GS(triangle GEOMETRY_INPUT input[3], inout TriangleStream<PIXEL_INPUT> OutputStream )
{
    PIXEL_INPUT output;
    float worldArea = findTriangleArea(input[0].Position, input[1].Position, input[2].Position);
    float uvArea = findTriangleArea(input[0].Texcoord, input[1].Texcoord, input[2].Texcoord);
    float textureArea = float(Map_Resolution_Size_Width) * float(Map_Resolution_Size_Height);
    float usedAreaPixels = uvArea * textureArea;
    float texelDensity = sqrt(usedAreaPixels/worldArea)
    float3 finalColor = GetColorOfTriangle(texelDensity);

    for( int i=0; i<3; i++ )
    {
        output.Position = input[i].Position;
        output.Texcoord = finalColor;

        OutputStream.Append( output );
    }
    
    OutputStream.RestartStrip();
}





float4 std_PS(PIXEL_INPUT input) : SV_Target
{
    // return diffuse
    return float4(input.Texcoord, 1.0);
}
///// TECHNIQUES /////////////////////////////
technique11 TexelDensity 
{
    pass p0 
    {
        SetVertexShader(CompileShader(vs_5_0,std_VS()));
        //SetGeometryShader(NULL);
        SetGeometryShader(CompileShader(gs_5_0,std_GS()));
        SetPixelShader(CompileShader(ps_5_0,std_PS()));
    }
}
/////////////////////////////////////// eof //