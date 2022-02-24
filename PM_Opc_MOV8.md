\== MOV = Move Register (8-Bits) ==

<table>
<tbody>
<tr class="odd">
<td><table>
<thead>
<tr class="header">
<th><p>Hex</p></th>
<th><p>Mnemonic</p></th>
<th><p>Cycles</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>40</p></td>
<td><p>MOV A, A</p></td>
<td><p>4</p></td>
</tr>
<tr class="even">
<td><p>41</p></td>
<td><p>MOV A, B</p></td>
<td><p>4</p></td>
</tr>
<tr class="odd">
<td><p>42</p></td>
<td><p>MOV A, L</p></td>
<td><p>4</p></td>
</tr>
<tr class="even">
<td><p>43</p></td>
<td><p>MOV A, H</p></td>
<td><p>4</p></td>
</tr>
<tr class="odd">
<td><p>44 nn</p></td>
<td><p>MOV A, [N+#nn]</p></td>
<td><p>12</p></td>
</tr>
<tr class="even">
<td><p>45</p></td>
<td><p>MOV A, [HL]</p></td>
<td><p>8</p></td>
</tr>
<tr class="odd">
<td><p>46</p></td>
<td><p>MOV A, [X]</p></td>
<td><p>8</p></td>
</tr>
<tr class="even">
<td><p>47</p></td>
<td><p>MOV A, [Y]</p></td>
<td><p>8</p></td>
</tr>
<tr class="odd">
<td><p>48</p></td>
<td><p>MOV B, A</p></td>
<td><p>4</p></td>
</tr>
<tr class="even">
<td><p>49</p></td>
<td><p>MOV B, B</p></td>
<td><p>4</p></td>
</tr>
<tr class="odd">
<td><p>4A</p></td>
<td><p>MOV B, L</p></td>
<td><p>4</p></td>
</tr>
<tr class="even">
<td><p>4B</p></td>
<td><p>MOV B, H</p></td>
<td><p>4</p></td>
</tr>
<tr class="odd">
<td><p>4C nn</p></td>
<td><p>MOV B, [N+#nn]</p></td>
<td><p>12</p></td>
</tr>
<tr class="even">
<td><p>4D</p></td>
<td><p>MOV B, [HL]</p></td>
<td><p>8</p></td>
</tr>
<tr class="odd">
<td><p>4E</p></td>
<td><p>MOV B, [X]</p></td>
<td><p>8</p></td>
</tr>
<tr class="even">
<td><p>4F</p></td>
<td><p>MOV B, [Y]</p></td>
<td><p>8</p></td>
</tr>
<tr class="odd">
<td><p>50</p></td>
<td><p>MOV L, A</p></td>
<td><p>4</p></td>
</tr>
<tr class="even">
<td><p>51</p></td>
<td><p>MOV L, B</p></td>
<td><p>4</p></td>
</tr>
<tr class="odd">
<td><p>52</p></td>
<td><p>MOV L, L</p></td>
<td><p>4</p></td>
</tr>
<tr class="even">
<td><p>53</p></td>
<td><p>MOV L, H</p></td>
<td><p>4</p></td>
</tr>
<tr class="odd">
<td><p>54 nn</p></td>
<td><p>MOV L, [N+#nn]</p></td>
<td><p>12</p></td>
</tr>
<tr class="even">
<td><p>55</p></td>
<td><p>MOV L, [HL]</p></td>
<td><p>8</p></td>
</tr>
<tr class="odd">
<td><p>56</p></td>
<td><p>MOV L, [X]</p></td>
<td><p>8</p></td>
</tr>
<tr class="even">
<td><p>57</p></td>
<td><p>MOV L, [Y]</p></td>
<td><p>8</p></td>
</tr>
<tr class="odd">
<td><p>58</p></td>
<td><p>MOV H, A</p></td>
<td><p>4</p></td>
</tr>
<tr class="even">
<td><p>59</p></td>
<td><p>MOV H, B</p></td>
<td><p>4</p></td>
</tr>
<tr class="odd">
<td><p>5A</p></td>
<td><p>MOV H, L</p></td>
<td><p>4</p></td>
</tr>
<tr class="even">
<td><p>5B</p></td>
<td><p>MOV H, H</p></td>
<td><p>4</p></td>
</tr>
<tr class="odd">
<td><p>5C nn</p></td>
<td><p>MOV H, [N+#nn]</p></td>
<td><p>12</p></td>
</tr>
<tr class="even">
<td><p>5D</p></td>
<td><p>MOV H, [HL]</p></td>
<td><p>8</p></td>
</tr>
<tr class="odd">
<td><p>5E</p></td>
<td><p>MOV H, [X]</p></td>
<td><p>8</p></td>
</tr>
<tr class="even">
<td><p>5F</p></td>
<td><p>MOV H, [Y]</p></td>
<td><p>8</p></td>
</tr>
<tr class="odd">
<td><p>60</p></td>
<td><p>MOV [X], A</p></td>
<td><p>8</p></td>
</tr>
<tr class="even">
<td><p>61</p></td>
<td><p>MOV [X], B</p></td>
<td><p>8</p></td>
</tr>
<tr class="odd">
<td><p>62</p></td>
<td><p>MOV [X], L</p></td>
<td><p>8</p></td>
</tr>
<tr class="even">
<td><p>63</p></td>
<td><p>MOV [X], H</p></td>
<td><p>8</p></td>
</tr>
<tr class="odd">
<td><p>64 nn</p></td>
<td><p>MOV [X], [N+#nn]</p></td>
<td><p>16</p></td>
</tr>
<tr class="even">
<td><p>65</p></td>
<td><p>MOV [X], [HL]</p></td>
<td><p>12</p></td>
</tr>
<tr class="odd">
<td><p>66</p></td>
<td><p>MOV [X], [X]</p></td>
<td><p>12</p></td>
</tr>
<tr class="even">
<td><p>67</p></td>
<td><p>MOV [X], [Y]</p></td>
<td><p>12</p></td>
</tr>
<tr class="odd">
<td><p>68</p></td>
<td><p>MOV [HL], A</p></td>
<td><p>8</p></td>
</tr>
<tr class="even">
<td><p>69</p></td>
<td><p>MOV [HL], B</p></td>
<td><p>8</p></td>
</tr>
<tr class="odd">
<td><p>6A</p></td>
<td><p>MOV [HL], L</p></td>
<td><p>8</p></td>
</tr>
<tr class="even">
<td><p>6B</p></td>
<td><p>MOV [HL], H</p></td>
<td><p>8</p></td>
</tr>
<tr class="odd">
<td><p>6C nn</p></td>
<td><p>MOV [HL], [N+#nn]</p></td>
<td><p>16</p></td>
</tr>
<tr class="even">
<td><p>6D</p></td>
<td><p>MOV [HL], [HL]</p></td>
<td><p>12</p></td>
</tr>
<tr class="odd">
<td><p>6E</p></td>
<td><p>MOV [HL], [X]</p></td>
<td><p>12</p></td>
</tr>
<tr class="even">
<td><p>6F</p></td>
<td><p>MOV [HL], [Y]</p></td>
<td><p>12</p></td>
</tr>
<tr class="odd">
<td><p>70</p></td>
<td><p>MOV [Y], A</p></td>
<td><p>8</p></td>
</tr>
<tr class="even">
<td><p>71</p></td>
<td><p>MOV [Y], B</p></td>
<td><p>8</p></td>
</tr>
<tr class="odd">
<td><p>72</p></td>
<td><p>MOV [Y], L</p></td>
<td><p>8</p></td>
</tr>
<tr class="even">
<td><p>73</p></td>
<td><p>MOV [Y], H</p></td>
<td><p>8</p></td>
</tr>
<tr class="odd">
<td><p>74 nn</p></td>
<td><p>MOV [Y], [N+#nn]</p></td>
<td><p>16</p></td>
</tr>
<tr class="even">
<td><p>75</p></td>
<td><p>MOV [Y], [HL]</p></td>
<td><p>12</p></td>
</tr>
<tr class="odd">
<td><p>76</p></td>
<td><p>MOV [Y], [X]</p></td>
<td><p>12</p></td>
</tr>
<tr class="even">
<td><p>77</p></td>
<td><p>MOV [Y], [Y]</p></td>
<td><p>12</p></td>
</tr>
<tr class="odd">
<td><p>78 nn</p></td>
<td><p>MOV [N+#nn], A</p></td>
<td><p>12</p></td>
</tr>
<tr class="even">
<td><p>79 nn</p></td>
<td><p>MOV [N+#nn], B</p></td>
<td><p>12</p></td>
</tr>
<tr class="odd">
<td><p>7A nn</p></td>
<td><p>MOV [N+#nn], L</p></td>
<td><p>12</p></td>
</tr>
<tr class="even">
<td><p>7B nn</p></td>
<td><p>MOV [N+#nn], H</p></td>
<td><p>12</p></td>
</tr>
<tr class="odd">
<td><p>7D nn</p></td>
<td><p>MOV [N+#nn], [HL]</p></td>
<td><p>16</p></td>
</tr>
<tr class="even">
<td><p>7E nn</p></td>
<td><p>MOV [N+#nn], [X]</p></td>
<td><p>16</p></td>
</tr>
<tr class="odd">
<td><p>7F nn</p></td>
<td><p>MOV [N+#nn], [Y]</p></td>
<td><p>16</p></td>
</tr>
<tr class="even">
<td><p>9F nn</p></td>
<td><p>MOV F, #nn</p></td>
<td><p>12</p></td>
</tr>
<tr class="odd">
<td><p>B0 nn</p></td>
<td><p>MOV A, #nn</p></td>
<td><p>8</p></td>
</tr>
<tr class="even">
<td><p>B1 nn</p></td>
<td><p>MOV B, #nn</p></td>
<td><p>8</p></td>
</tr>
<tr class="odd">
<td><p>B2 nn</p></td>
<td><p>MOV L, #nn</p></td>
<td><p>8</p></td>
</tr>
<tr class="even">
<td><p>B3 nn</p></td>
<td><p>MOV H, #nn</p></td>
<td><p>8</p></td>
</tr>
<tr class="odd">
<td><p>B4 nn</p></td>
<td><p>MOV N, #nn</p></td>
<td><p>8</p></td>
</tr>
<tr class="even">
<td><p>B5 nn</p></td>
<td><p>MOV [HL], #nn</p></td>
<td><p>12</p></td>
</tr>
<tr class="odd">
<td><p>B6 nn</p></td>
<td><p>MOV [X], #nn</p></td>
<td><p>12</p></td>
</tr>
<tr class="even">
<td><p>B7 nn</p></td>
<td><p>MOV [Y], #nn</p></td>
<td><p>12</p></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table></td>
<td><table>
<thead>
<tr class="header">
<th><p>Hex</p></th>
<th><p>Mnemonic</p></th>
<th><p>Cycles</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>DD nn nn</p></td>
<td><p>MOV [N+#nn], #nn</p></td>
<td><p>16</p></td>
</tr>
<tr class="even">
<td><p>CE C4 nn</p></td>
<td><p>MOV U, #nn</p></td>
<td><p>16</p></td>
</tr>
<tr class="odd">
<td><p>CE C5 nn</p></td>
<td><p>MOV I, #nn</p></td>
<td><p>12</p></td>
</tr>
<tr class="even">
<td><p>CE C6 nn</p></td>
<td><p>MOV XI, #nn</p></td>
<td><p>12</p></td>
</tr>
<tr class="odd">
<td><p>CE C7 nn</p></td>
<td><p>MOV YI, #nn</p></td>
<td><p>12</p></td>
</tr>
<tr class="even">
<td><p>CE 40 ss</p></td>
<td><p>MOV A, [X+#ss]</p></td>
<td><p>16</p></td>
</tr>
<tr class="odd">
<td><p>CE 41 ss</p></td>
<td><p>MOV A, [Y+#ss]</p></td>
<td><p>16</p></td>
</tr>
<tr class="even">
<td><p>CE 42</p></td>
<td><p>MOV A, [X+L]</p></td>
<td><p>16</p></td>
</tr>
<tr class="odd">
<td><p>CE 43</p></td>
<td><p>MOV A, [Y+L]</p></td>
<td><p>16</p></td>
</tr>
<tr class="even">
<td><p>CE 48 ss</p></td>
<td><p>MOV B, [X+#ss]</p></td>
<td><p>16</p></td>
</tr>
<tr class="odd">
<td><p>CE 49 ss</p></td>
<td><p>MOV B, [Y+#ss]</p></td>
<td><p>16</p></td>
</tr>
<tr class="even">
<td><p>CE 4A</p></td>
<td><p>MOV B, [X+L]</p></td>
<td><p>16</p></td>
</tr>
<tr class="odd">
<td><p>CE 4B</p></td>
<td><p>MOV B, [Y+L]</p></td>
<td><p>16</p></td>
</tr>
<tr class="even">
<td><p>CE 50 ss</p></td>
<td><p>MOV L, [X+#ss]</p></td>
<td><p>16</p></td>
</tr>
<tr class="odd">
<td><p>CE 51 ss</p></td>
<td><p>MOV L, [Y+#ss]</p></td>
<td><p>16</p></td>
</tr>
<tr class="even">
<td><p>CE 52</p></td>
<td><p>MOV L, [X+L]</p></td>
<td><p>16</p></td>
</tr>
<tr class="odd">
<td><p>CE 53</p></td>
<td><p>MOV L, [Y+L]</p></td>
<td><p>16</p></td>
</tr>
<tr class="even">
<td><p>CE 58 ss</p></td>
<td><p>MOV H, [X+#ss]</p></td>
<td><p>16</p></td>
</tr>
<tr class="odd">
<td><p>CE 59 ss</p></td>
<td><p>MOV H, [Y+#ss]</p></td>
<td><p>16</p></td>
</tr>
<tr class="even">
<td><p>CE 5A</p></td>
<td><p>MOV H, [X+L]</p></td>
<td><p>16</p></td>
</tr>
<tr class="odd">
<td><p>CE 5B</p></td>
<td><p>MOV H, [Y+L]</p></td>
<td><p>16</p></td>
</tr>
<tr class="even">
<td><p>CE 44 ss</p></td>
<td><p>MOV [X+#ss], A</p></td>
<td><p>16</p></td>
</tr>
<tr class="odd">
<td><p>CE 45 ss</p></td>
<td><p>MOV [Y+#ss], A</p></td>
<td><p>16</p></td>
</tr>
<tr class="even">
<td><p>CE 46</p></td>
<td><p>MOV [X+L], A</p></td>
<td><p>16</p></td>
</tr>
<tr class="odd">
<td><p>CE 47</p></td>
<td><p>MOV [Y+L], A</p></td>
<td><p>16</p></td>
</tr>
<tr class="even">
<td><p>CE 4C ss</p></td>
<td><p>MOV [X+#ss], B</p></td>
<td><p>16</p></td>
</tr>
<tr class="odd">
<td><p>CE 4D ss</p></td>
<td><p>MOV [Y+#ss], B</p></td>
<td><p>16</p></td>
</tr>
<tr class="even">
<td><p>CE 4E</p></td>
<td><p>MOV [X+L], B</p></td>
<td><p>16</p></td>
</tr>
<tr class="odd">
<td><p>CE 4F</p></td>
<td><p>MOV [Y+L], B</p></td>
<td><p>16</p></td>
</tr>
<tr class="even">
<td><p>CE 54 ss</p></td>
<td><p>MOV [X+#ss], L</p></td>
<td><p>16</p></td>
</tr>
<tr class="odd">
<td><p>CE 55 ss</p></td>
<td><p>MOV [Y+#ss], L</p></td>
<td><p>16</p></td>
</tr>
<tr class="even">
<td><p>CE 56</p></td>
<td><p>MOV [X+L], L</p></td>
<td><p>16</p></td>
</tr>
<tr class="odd">
<td><p>CE 57</p></td>
<td><p>MOV [Y+L], L</p></td>
<td><p>16</p></td>
</tr>
<tr class="even">
<td><p>CE 5C ss</p></td>
<td><p>MOV [X+#ss], H</p></td>
<td><p>16</p></td>
</tr>
<tr class="odd">
<td><p>CE 5D ss</p></td>
<td><p>MOV [Y+#ss], H</p></td>
<td><p>16</p></td>
</tr>
<tr class="even">
<td><p>CE 5E</p></td>
<td><p>MOV [X+L], H</p></td>
<td><p>16</p></td>
</tr>
<tr class="odd">
<td><p>CE 5F</p></td>
<td><p>MOV [Y+L], H</p></td>
<td><p>16</p></td>
</tr>
<tr class="even">
<td><p>CE 60 ss</p></td>
<td><p>MOV [HL], [X+#ss]</p></td>
<td><p>20</p></td>
</tr>
<tr class="odd">
<td><p>CE 61 ss</p></td>
<td><p>MOV [HL], [Y+#ss]</p></td>
<td><p>20</p></td>
</tr>
<tr class="even">
<td><p>CE 62</p></td>
<td><p>MOV [HL], [X+L]</p></td>
<td><p>20</p></td>
</tr>
<tr class="odd">
<td><p>CE 63</p></td>
<td><p>MOV [HL], [Y+L]</p></td>
<td><p>20</p></td>
</tr>
<tr class="even">
<td><p>CE 68 ss</p></td>
<td><p>MOV [X], [X+#ss]</p></td>
<td><p>20</p></td>
</tr>
<tr class="odd">
<td><p>CE 69 ss</p></td>
<td><p>MOV [X], [Y+#ss]</p></td>
<td><p>20</p></td>
</tr>
<tr class="even">
<td><p>CE 6A</p></td>
<td><p>MOV [X], [X+L]</p></td>
<td><p>20</p></td>
</tr>
<tr class="odd">
<td><p>CE 6B</p></td>
<td><p>MOV [X], [Y+L]</p></td>
<td><p>20</p></td>
</tr>
<tr class="even">
<td><p>CE 78 ss</p></td>
<td><p>MOV [Y], [X+#ss]</p></td>
<td><p>20</p></td>
</tr>
<tr class="odd">
<td><p>CE 79 ss</p></td>
<td><p>MOV [Y], [Y+#ss]</p></td>
<td><p>20</p></td>
</tr>
<tr class="even">
<td><p>CE 7A</p></td>
<td><p>MOV [Y], [X+L]</p></td>
<td><p>20</p></td>
</tr>
<tr class="odd">
<td><p>CE 7B</p></td>
<td><p>MOV [Y], [Y+L]</p></td>
<td><p>20</p></td>
</tr>
<tr class="even">
<td><p>CE C0</p></td>
<td><p>MOV A, N</p></td>
<td><p>8</p></td>
</tr>
<tr class="odd">
<td><p>CE C1</p></td>
<td><p>MOV A, F</p></td>
<td><p>8</p></td>
</tr>
<tr class="even">
<td><p>CE C8</p></td>
<td><p>MOV A, V</p></td>
<td><p>8</p></td>
</tr>
<tr class="odd">
<td><p>CE C9</p></td>
<td><p>MOV A, I</p></td>
<td><p>8</p></td>
</tr>
<tr class="even">
<td><p>CE CA</p></td>
<td><p>MOV A, XI</p></td>
<td><p>8</p></td>
</tr>
<tr class="odd">
<td><p>CE CB</p></td>
<td><p>MOV A, YI</p></td>
<td><p>8</p></td>
</tr>
<tr class="even">
<td><p>CE C2</p></td>
<td><p>MOV N, A</p></td>
<td><p>8</p></td>
</tr>
<tr class="odd">
<td><p>CE C3</p></td>
<td><p>MOV F, A</p></td>
<td><p>12</p></td>
</tr>
<tr class="even">
<td><p>CE CC</p></td>
<td><p>MOV U, A</p></td>
<td><p>12</p></td>
</tr>
<tr class="odd">
<td><p>CE CD</p></td>
<td><p>MOV I, A</p></td>
<td><p>8</p></td>
</tr>
<tr class="even">
<td><p>CE CE</p></td>
<td><p>MOV XI, A</p></td>
<td><p>8</p></td>
</tr>
<tr class="odd">
<td><p>CE CF</p></td>
<td><p>MOV YI, A</p></td>
<td><p>8</p></td>
</tr>
<tr class="even">
<td><p>CE D0 nn nn</p></td>
<td><p>MOV A, [#nnnn]</p></td>
<td><p>20</p></td>
</tr>
<tr class="odd">
<td><p>CE D1 nn nn</p></td>
<td><p>MOV B, [#nnnn]</p></td>
<td><p>20</p></td>
</tr>
<tr class="even">
<td><p>CE D2 nn nn</p></td>
<td><p>MOV L, [#nnnn]</p></td>
<td><p>20</p></td>
</tr>
<tr class="odd">
<td><p>CE D3 nn nn</p></td>
<td><p>MOV H, [#nnnn]</p></td>
<td><p>20</p></td>
</tr>
<tr class="even">
<td><p>CE D4 nn nn</p></td>
<td><p>MOV [#nnnn], A</p></td>
<td><p>20</p></td>
</tr>
<tr class="odd">
<td><p>CE D5 nn nn</p></td>
<td><p>MOV [#nnnn], B</p></td>
<td><p>20</p></td>
</tr>
<tr class="even">
<td><p>CE D6 nn nn</p></td>
<td><p>MOV [#nnnn], L</p></td>
<td><p>20</p></td>
</tr>
<tr class="odd">
<td><p>CE D7 nn nn</p></td>
<td><p>MOV [#nnnn], H</p></td>
<td><p>20</p></td>
</tr>
<tr class="even">
<td><p> </p></td>
<td><p> </p></td>
<td><p> </p></td>
</tr>
<tr class="odd">
<td><p> </p></td>
<td><p> </p></td>
<td><p> </p></td>
</tr>
<tr class="even">
<td><p> </p></td>
<td><p> </p></td>
<td><p> </p></td>
</tr>
</tbody>
</table></td>
</tr>
</tbody>
</table>

**Source as the column, and Destination as the
row:**

|            | \#nn       | A           | B           | L           | H           | N          | F          | V       | I       | XI    | YI    |
| ---------- | ---------- | ----------- | ----------- | ----------- | ----------- | ---------- | ---------- | ------- | ------- | ----- | ----- |
| A          | B0 nn      | 40          | 41          | 42          | 43          | CE C0      | CE C1      | CE C8   | CE C9   | CE CA | CE CB |
| B          | B1 nn      | 48          | 49          | 4A          | 4B          |            |            |         |         |       |       |
| L          | B2 nn      | 50          | 51          | 52          | 53          |            |            |         |         |       |       |
| H          | B3 nn      | 58          | 59          | 5A          | 5B          |            |            |         |         |       |       |
| N          | B4 nn      | CE C2       |             |             |             |            |            |         |         |       |       |
| F          | 9F nn      | CE C3       |             |             |             |            |            |         |         |       |       |
| U          | CE C4 nn   | CE CC       |             |             |             |            |            |         |         |       |       |
| I          | CE C5 nn   | CE CD       |             |             |             |            |            |         |         |       |       |
| XI         | CE C6 nn   | CE CE       |             |             |             |            |            |         |         |       |       |
| YI         | CE C7 nn   | CE CF       |             |             |             |            |            |         |         |       |       |
| \[N+\#nn\] | DD nn nn   | 78 nn       | 79 nn       | 7A nn       | 7B nn       |            |            |         |         |       |       |
| \[HL\]     | B5 nn      | 68          | 69          | 6A          | 6B          |            |            |         |         |       |       |
| \[X\]      | B6 nn      | 60          | 61          | 62          | 63          |            |            |         |         |       |       |
| \[Y\]      | B7 nn      | 70          | 71          | 72          | 73          |            |            |         |         |       |       |
| \[\#nnnn\] |            | CE D4 nn nn | CE D5 nn nn | CE D6 nn nn | CE D7 nn nn |            |            |         |         |       |       |
| \[X+\#ss\] |            | CE 44 ss    | CE 4C ss    | CE 54 ss    | CE 5C ss    |            |            |         |         |       |       |
| \[Y+\#ss\] |            | CE 45 ss    | CE 4D ss    | CE 55 ss    | CE 5D ss    |            |            |         |         |       |       |
| \[X+L\]    |            | CE 46       | CE 4E       | CE 56       | CE 5E ss    |            |            |         |         |       |       |
| \[Y+L\]    |            | CE 47       | CE 4F       | CE 57       | CE 5F ss    |            |            |         |         |       |       |
|            |            |             |             |             |             |            |            |         |         |       |       |
|            | \[N+\#nn\] | \[HL\]      | \[X\]       | \[Y\]       | \[\#nnnn\]  | \[X+\#ss\] | \[Y+\#ss\] | \[X+L\] | \[Y+L\] |       |       |
| A          | 44 nn      | 45          | 46          | 47          | CE D0 nn nn | CE 40 ss   | CE 41 ss   | CE 42   | CE 43   |       |       |
| B          | 4C nn      | 4D          | 4E          | 4F          | CE D1 nn nn | CE 48 ss   | CE 49 ss   | CE 4A   | CE 4B   |       |       |
| L          | 54 nn      | 55          | 56          | 57          | CE D2 nn nn | CE 50 ss   | CE 51 ss   | CE 52   | CE 53   |       |       |
| H          | 5C nn      | 5D          | 5E          | 5F          | CE D3 nn nn | CE 58 ss   | CE 59 ss   | CE 5A   | CE 5B   |       |       |
| N          |            |             |             |             |             |            |            |         |         |       |       |
| F          |            |             |             |             |             |            |            |         |         |       |       |
| U          |            |             |             |             |             |            |            |         |         |       |       |
| I          |            |             |             |             |             |            |            |         |         |       |       |
| XI         |            |             |             |             |             |            |            |         |         |       |       |
| YI         |            |             |             |             |             |            |            |         |         |       |       |
| \[N+\#nn\] |            | 7D nn       | 7E nn       | 7F nn       |             |            |            |         |         |       |       |
| \[HL\]     | 6C nn      | 6D          | 6E          | 6F          |             | CE 60 ss   | CE 61 ss   | CE 62   | CE 63   |       |       |
| \[X\]      | 64 nn      | 65          | 66          | 67          |             | CE 68 ss   | CE 69 ss   | CE 6A   | CE 6B   |       |       |
| \[Y\]      | 74 nn      | 75          | 76          | 77          |             | CE 78 ss   | CE 79 ss   | CE 7A   | CE 7B   |       |       |
| \[\#nnnn\] |            |             |             |             |             |            |            |         |         |       |       |
| \[X+\#ss\] |            |             |             |             |             |            |            |         |         |       |       |
| \[Y+\#ss\] |            |             |             |             |             |            |            |         |         |       |       |
| \[X+L\]    |            |             |             |             |             |            |            |         |         |       |       |
| \[Y+L\]    |            |             |             |             |             |            |            |         |         |       |       |

### Execute

`#nn     = Immediate unsigned 8-Bits`
`#ss     = Immediate signed 8-Bits`
`A       = Register A`
`B       = Register B`
`L       = Register L`
`H       = Register H`
`N       = Register N`
`F       = Register F`
`U/V     = Register U or V`
`I       = Register I`
`XI      = Register XI`
`YI      = Register YI`
`[N+#nn] = Memory: (I shl 16) or (N shl 8) or #nn`
`[HL]    = Memory: (I shl 16) or HL`
`[X]     = Memory: (XI shl 16) or X`
`[Y]     = Memory: (YI shl 16) or Y`
`[#nnnn] = Memory: #nnnn`
`[X+#ss] = Memory: (XI shl 16) or (X + #ss)`
`[Y+#ss] = Memory: (YI shl 16) or (Y + #ss)`
`[X+L]   = Memory: (XI shl 16) or (X + signed(L))`
`[Y+L]   = Memory: (YI shl 16) or (Y + signed(L))`

`; MOV Ds, Sc`
`;`
`; Ds = Destination`
`; Sc = Source`

`Ds = Sc`

### Description

8-Bits Source gets copied to the 8-Bits Destination.

### Conditions

None

### Examples

`; A = 0x55`
**`MOV`` ``A,`` ``$80`**
`; A = 0x80`

`; A = 0x12`
`; B = 0xCF`
**`MOV`` ``B,`` ``A`**
`; A = 0x12`
`; B = 0x12`

`; [HL] = 0xDE`
`; A = 0xCF`
**`MOV`` ``A,`` ``[HL]`**
`; [HL] = 0xDE`
`; A = 0xDE`

[**« Back to Instruction set**](S1C88_InstructionSet.md "wikilink")
